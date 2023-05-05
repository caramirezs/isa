import qrcode

url = "https://www.ejemplo.com" # reemplaza esta dirección web por la que quieras convertir en QR

img = qrcode.make(url)
img.save("qr_code.png") # guarda el código QR en un archivo png