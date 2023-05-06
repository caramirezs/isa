import qrcode

url = "https://drive.google.com/file/d/1XJZsXXenerlsedsPK3yNf888Hbfc296_/view?usp=sharing" # reemplaza esta dirección web por la que quieras convertir en QR

img = qrcode.make(url)
img.save("qr_regalo_fin.png") # guarda el código QR en un archivo png