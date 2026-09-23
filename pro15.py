import qrcode
data=input("Enter link or text to generate QR code: ")
img=qrcode.make("data")
img.save("img.png")
img.show()
print("QR code generated and saved as img.png")