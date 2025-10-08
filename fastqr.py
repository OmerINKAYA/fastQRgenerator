import qrcode
from PIL import Image

# Variable'ları belirle, çalıştır
data = "https://atiknakit.com/"
logo_file = "logo_green.png"
output_filename = "qr_with_logo.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGBA')



try:
    logo = Image.open(logo_file)
except FileNotFoundError:
    print("Error: 'logo_green.png' not found. Please check the file path.")
    exit()

if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')

datas = logo.getdata()
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
logo.putdata(newData)

qr_width, qr_height = img_qr.size
logo_max_size = qr_height // 4

logo.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)

logo_x = (qr_width - logo.width) // 2
logo_y = (qr_height - logo.height) // 2

img_qr.paste(logo, (logo_x, logo_y), logo)

img_qr.save(output_filename)

print(f"Successfully created QR code with logo: {output_filename}")