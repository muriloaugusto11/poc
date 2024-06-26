import qrcode

# Dados para o QR Code
data = "http://127.0.0.1:5000/"

# Crie a instância do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicione os dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Crie a imagem do QR Code
img = qr.make_image(fill_color="red", back_color="black")

# Salve a imagem
img.save("qrcode.png")

# Mostrar a imagem (opcional)
img.show()
