import qrcode

# URL de ta page GitHub
url = "https://klibres300-art.github.io/linkartist/"

# Création du QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Génération de l'image
img = qr.make_image(fill_color="black", back_color="white")
img.save("github_page_qr.png")

print("QR code généré : github_page_qr.png")
