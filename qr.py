import qrcode as qr

img = qr.make("https://www.rejinadahal.com.np/")
img.save("rejina_website.png")