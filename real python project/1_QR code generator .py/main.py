import qrcode as qr  # Importing the 'qrcode' module and aliasing it as 'qr'

# Creating a QR code with the specified URL
img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrl")

# Saving the generated QR code as an image file
img.save("QRcode_project_youtube_video.png")

