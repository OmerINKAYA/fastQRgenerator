# QR Code Generator with Logo

A Python script that generates QR codes with custom logos embedded in the center.

## Features

- Generate QR codes for any text or URL
- Embed custom logos in the center of QR codes
- Automatic logo transparency handling (removes black backgrounds)
- High error correction for better scanning reliability
- Simple configuration through code variables

## 🚀 Quick Start (After Cloning)

### Clone to Desktop and Run:

```bash
# Clone the repository to Desktop
cd ~/Desktop
git clone https://github.com/YOUR_USERNAME/QRCode.git
cd QRCode

# Set up and run (one-time setup)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run the script
python fastqr.py
```

**That's it!** Your QR code will be saved as `qr_with_logo.png`

### For Windows Users:
```cmd
cd %USERPROFILE%\Desktop
git clone https://github.com/YOUR_USERNAME/QRCode.git
cd QRCode
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python fastqr.py
```

## Requirements

- Python 3.6 or higher
- Git (for cloning)

## 🎯 Usage

### Run with Default Settings (Fastest):
```bash
python fastqr.py
```
This creates a QR code for "https://atiknakit.com/" using `logo_green.png` → saves as `qr_with_logo.png`

### Customize Your QR Code:
Edit the variables at the top of `fastqr.py`:
```python
data = "https://atiknakit.com/"     # Change this to your URL or text
logo_file = "logo_green.png"        # Change this to your logo filename  
output_filename = "qr_with_logo.png" # Change output filename
```

Then run:
```bash
python fastqr.py
```

### Test with Sample Logo:
```python
logo_file = "sample_logo.png"  # Use the included sample logo
```

## How It Works

The script:
1. Creates a QR code with high error correction
2. Opens your logo file
3. Automatically removes black backgrounds from the logo (makes them transparent)
4. Resizes the logo to 1/4 of the QR code size
5. Centers the logo on the QR code
6. Saves the final image

## 📁 File Structure

```
QRCode/
├── fastqr.py              # Main script (edit variables here)
├── requirements.txt       # Python dependencies  
├── README.md             # This file
├── EXAMPLES.md           # Example files documentation
├── logo_green.png        # Original logo file
├── sample_logo.png       # Sample logo for testing
└── qr_with_logo.png      # Generated QR code output (after running)
```

## ⚡ One-Line Setup (Copy & Paste)

**macOS/Linux:**
```bash
cd ~/Desktop && git clone https://github.com/YOUR_USERNAME/QRCode.git && cd QRCode && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python fastqr.py
```

**Windows:**
```cmd
cd %USERPROFILE%\Desktop && git clone https://github.com/YOUR_USERNAME/QRCode.git && cd QRCode && python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt && python fastqr.py
```

## 🔧 Troubleshooting

- **"'logo_green.png' not found"**: Make sure you're in the QRCode folder when running
- **"python not found"**: Install Python from [python.org](https://python.org)
- **"git not found"**: Install Git from [git-scm.com](https://git-scm.com)
- **Virtual environment issues**: Skip venv and run `pip install qrcode pillow` directly

## 📦 Dependencies

- `qrcode==8.2`: For generating QR codes
- `pillow==11.3.0`: For image processing and logo handling

## 💡 Tips

- ✅ Works immediately after cloning - no setup needed beyond installing packages
- ✅ Use high-contrast logos for best scanning results
- ✅ Black backgrounds in logos are automatically made transparent
- ✅ Logo is auto-resized to perfect size (1/4 of QR code height)
- ✅ High error correction means QR codes work even with logos