from flask import Flask, request, render_template, jsonify
import base64, binascii, hashlib, io, urllib.parse
from PIL import Image, UnidentifiedImageError
import qrcode
from stegano import lsb

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        action = request.form.get('action')
        encoding = request.form.get('encoding')
        result = ""
        image_data_url = None

        if action == 'encode':
            image = request.files.get('image')

            if not image or not allowed_file(image.filename):
                return jsonify({'error': 'Unsupported or missing image file.'})

            img_bytes = image.read()

            try:
                img = Image.open(io.BytesIO(img_bytes))
            except UnidentifiedImageError:
                return jsonify({'error': 'Invalid image file.'})

            if encoding == 'base64':
                result = base64.b64encode(img_bytes).decode('utf-8')

            elif encoding == 'hex':
                result = binascii.hexlify(img_bytes).decode('utf-8')

            elif encoding == 'binary':
                result = ''.join(format(b, '08b') for b in img_bytes)

            elif encoding == 'url':
                result = urllib.parse.quote_from_bytes(img_bytes)

            elif encoding == 'ascii':
                img = img.convert('L')
                img = img.resize((100, 50))
                chars = "@%#*+=-:. "
                ascii_art = ""
                for y in range(img.height):
                    for x in range(img.width):
                        ascii_art += chars[img.getpixel((x, y)) // 25]
                    ascii_art += '\n'
                result = ascii_art

            elif encoding == 'md5':
                result = hashlib.md5(img_bytes).hexdigest()

            elif encoding == 'sha256':
                result = hashlib.sha256(img_bytes).hexdigest()

            elif encoding == 'qr':
                name = image.filename
                qr_img = qrcode.make(name)
                buf = io.BytesIO()
                qr_img.save(buf, format='PNG')
                image_data_url = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode('utf-8')
                result = "QR code generated from filename."

            elif encoding == 'stegano':
                text_to_hide = request.form.get('steg_text')
                if not text_to_hide:
                    return jsonify({'error': 'Please provide text to hide for steganography.'})
                encoded_img = lsb.hide(img, text_to_hide)
                buf = io.BytesIO()
                encoded_img.save(buf, format='PNG')
                image_data_url = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode('utf-8')
                result = "Text hidden in image successfully."

        elif action == 'decode':
            if encoding in ['md5', 'sha256']:
                return jsonify({'error': f"Cannot decode hash function {encoding.upper()}."})

            if encoding == 'stegano':
                image = request.files.get('image')
                if not image or not allowed_file(image.filename):
                    return jsonify({'error': 'Image required for steganography decoding.'})
                try:
                    img = Image.open(image)
                    hidden = lsb.reveal(img)
                except UnidentifiedImageError:
                    return jsonify({'error': 'Invalid image file.'})
                except Exception as e:
                    return jsonify({'error': f'Error during steganography decoding: {str(e)}'})
                
                result = hidden or "No hidden message found."

            else:
                code_text = request.form.get('code_text', '').strip()
                if not code_text:
                    return jsonify({'error': 'Please provide encoded text to decode.'})

                try:
                    if encoding == 'base64':
                        img_bytes = base64.b64decode(code_text)
                        
                    elif encoding == 'hex':
                        img_bytes = binascii.unhexlify(code_text)
                        
                    elif encoding == 'binary':
                        # Ensure binary string length is multiple of 8
                        if len(code_text) % 8 != 0:
                            return jsonify({'error': 'Binary string length must be multiple of 8.'})
                        byte_data = int(code_text, 2).to_bytes((len(code_text) + 7) // 8, byteorder='big')
                        img_bytes = byte_data
                        
                    elif encoding == 'url':
                        img_bytes = urllib.parse.unquote_to_bytes(code_text)
                    
                    # Validate that the decoded bytes form a valid image
                    try:
                        test_img = Image.open(io.BytesIO(img_bytes))
                        test_img.verify()  # Verify it's a valid image
                    except:
                        return jsonify({'error': 'Decoded data does not form a valid image.'})
                    
                    # Create data URL for the decoded image
                    image_data_url = "data:image/png;base64," + base64.b64encode(img_bytes).decode('utf-8')
                    result = "success"  # We'll handle this in frontend
                    
                except binascii.Error:
                    return jsonify({'error': f'Invalid {encoding.upper()} format.'})
                except ValueError as e:
                    return jsonify({'error': f'Invalid {encoding.upper()} data: {str(e)}'})
                except Exception as e:
                    return jsonify({'error': f'Error decoding {encoding.upper()}: {str(e)}'})

        return jsonify({'result': result, 'image_data_url': image_data_url})

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)