import qrcode

url = "https://drive.google.com/file/d/1YGltgWt_c-uYhc1qFsBHSojogS_WbJzv/view?usp=sharing" # reemplaza esta dirección web por la que quieras convertir en QR

img = qrcode.make(url)
img.save("static/documento.png") # guarda el código QR en un archivo png