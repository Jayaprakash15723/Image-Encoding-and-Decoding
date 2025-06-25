# Image-Encoding-and-Decoding
A Image Encode and Decoder


# 🖼️ Image Encoder/Decoder Tool

A powerful web application that allows you to encode images into various text formats and decode them back to images.

## ✨ Features

### Encoding Options
- **Base64** - Convert images to Base64 text format
- **Hexadecimal** - Convert images to hex string representation
- **Binary** - Convert images to binary (0s and 1s) format
- **URL Encoding** - URL-safe encoding of image data
- **ASCII Art** - Convert images to text-based ASCII art
- **MD5 Hash** - Generate MD5 hash of image data
- **SHA256 Hash** - Generate SHA256 hash of image data
- **QR Code** - Generate QR code from image filename
- **Steganography** - Hide secret text messages inside images

### Decoding Options
- **Base64 to Image** - Decode Base64 text back to image
- **Hex to Image** - Decode hexadecimal string back to image
- **Binary to Image** - Decode binary string back to image
- **URL to Image** - Decode URL-encoded data back to image
- **Steganography** - Reveal hidden messages from images

### User Experience
- 🚫 **No annoying pop-ups** - Clean notification system
- 📋 **One-click copying** - Copy text and images to clipboard
- ⬇️ **Easy downloads** - Download processed images instantly
- 📱 **Responsive design** - Works on desktop and mobile
- ✨ **Modern UI** - Bootstrap-powered interface

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/image-encoder-decoder.git
   cd image-encoder-decoder
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   http://localhost:5000
   ```

## 📦 Dependencies

```
Flask==2.3.3
Pillow==10.0.1
qrcode==7.4.2
stegano==0.10.2
```

## 🏗️ Project Structure

```
image-encoder-decoder/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── templates/
│   └── index.html        # Main HTML template
│
└── static/ (optional)
    ├── css/
    ├── js/
    └── images/
```

## 🔧 Usage Guide

### Encoding an Image

1. Select **"Encode"** from the action dropdown
2. Upload your image file (supports PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP)
3. Choose your desired encoding format
4. Click **"Submit"**
5. Copy the generated text or download the result

### Decoding Text to Image

1. Select **"Decode"** from the action dropdown
2. Paste your encoded text in the text area
3. Select the matching encoding format
4. Click **"Submit"**
5. View, copy, or download the decoded image

### Steganography

**Hide a message:**
1. Select **"Encode"** → **"Steganography"**
2. Upload an image
3. Enter your secret message
4. Download the image with hidden message

**Reveal a message:**
1. Select **"Decode"** → **"Steganography"**
2. Upload the image containing hidden message
3. The secret message will be displayed

## 🌐 Deployment

### Local Development
```bash
export FLASK_ENV=development
python app.py
```

### Production Deployment

#### Option 1: Render.com
1. Connect your GitHub repository to Render
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

#### Option 2: Railway.app
1. Connect repository to Railway
2. Railway will auto-detect Flask app
3. Deploy automatically

#### Option 3: PythonAnywhere
1. Upload files to PythonAnywhere
2. Set up web app with Flask
3. Install dependencies in console

## 🛠️ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/process` | POST | Process encoding/decoding requests |

### API Request Format
```javascript
// Form data for /process endpoint
{
  action: 'encode' | 'decode',
  encoding: 'base64' | 'hex' | 'binary' | 'url' | 'ascii' | 'md5' | 'sha256' | 'qr' | 'stegano',
  image: File (for encoding),
  code_text: String (for decoding),
  steg_text: String (for steganography encoding)
}
```

### API Response Format
```javascript
{
  result: String,           // Encoded text or success message
  image_data_url: String,   // Data URL for images
  error: String            // Error message if any
}
```

## 🔒 Security Features

- **File validation** - Only allows supported image formats
- **Input sanitization** - Validates all user inputs
- **Error handling** - Comprehensive error catching and reporting
- **Safe decoding** - Validates decoded data before processing

## 🎯 Supported File Formats

**Input Images:**
- PNG, JPG, JPEG
- BMP, GIF, TIFF
- WEBP

**Output Formats:**
- All encoding results as downloadable text files
- Decoded images as PNG format
- QR codes as PNG images
- Steganography results as PNG images

## 🐛 Troubleshooting

### Common Issues

**"Invalid image file" error:**
- Make sure file is a supported image format
- Check if image file is corrupted

**"Cannot decode" error:**
- Verify the encoding format matches the encoded text
- Check if encoded text is complete and not corrupted

**Steganography not working:**
- Ensure the image has sufficient capacity for the message
- Use PNG format for best steganography results

**Installation issues:**
```bash
# If Pillow fails to install
pip install --upgrade pip
pip install Pillow

# If stegano fails to install
pip install --upgrade setuptools
pip install stegano
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Pillow](https://pillow.readthedocs.io/) - Image processing
- [qrcode](https://github.com/lincolnloop/python-qrcode) - QR code generation
- [stegano](https://github.com/cedricbonhomme/Stegano) - Steganography functionality
- [Bootstrap](https://getbootstrap.com/) - UI framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/image-encoder-decoder/issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

---

⭐ **Star this repository if you found it helpful!**
