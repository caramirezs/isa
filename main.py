from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import subprocess
import time, os
from datetime import datetime

script_path = "/home/caramirezs/rpi-rgb-led-matrix/my_clock.py"
script_path_2 = "/home/caramirezs/rpi-rgb-led-matrix/mensaje1.py"
script_path_3 = "/home/caramirezs/rpi-rgb-led-matrix/bindings/python/samples/runtext.py slitherin"
script_directory = os.path.dirname(script_path)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Encontraste el Luminaris!!!')


@app.route('/send_email', methods=['POST'])
def send_email():
    from_address = 'kamandramsan@hotmail.com'
    to_address_1 = 'leidyna25@hotmail.com' # Julieta
    to_address_2 = 'santoymontero@gmail.com' # Santiago
    password = 'mlk6456And'
    message_1 = """
    Hola, Julieta. Isabella te ha contactado para pedirte ayuda en una emocionante búsqueda del tesoro.
    Juntas, deben resolver un acertijo para encontrar un artilugio mágico escondido en Hogwarts. 
    Para tener éxito, necesitarán colaborar y confiar en sus habilidades mágicas y conocimientos del mundo mágico.
    El acertijo que deben resolver es el siguiente:
    "¿En qué fecha (MMDDAAAA) vio Isabella por primera vez al profesor Mylo?" 
    Parece sencillo, ¿no?
    
    Reflexionen juntas sobre sus recuerdos y conocimientos de Hogwarts para descifrar la fecha en la que Isabella conoció al profesor Mylo. Una vez que hayan resuelto el acertijo, utilicen la fecha como contraseña para desbloquear un archivo secreto. 
    Dentro del archivo, encontrarán pistas que las guiarán hacia el artilugio mágico escondido.
    
    Recuerden trabajar juntas y apoyarse mutuamente en esta aventura. 
    ¡Que la magia las acompañe!
    
    """
    message_2 = """
    Hola, Santiago. Isabella te ha contactado para pedirte ayuda en una emocionante búsqueda del tesoro.
    Juntos, deben resolver un acertijo para encontrar un artilugio mágico escondido en Hogwarts. 
    Para tener éxito, necesitarán colaborar y confiar en sus habilidades mágicas y conocimientos del mundo mágico.
    El acertijo que deben resolver es el siguiente:
    "¿En qué fecha (MMDDAAAA) nació la mascota preferida de Hogwarts?" 
    Parece sencillo, ¿no?
    
    Reflexionen juntas sobre sus recuerdos y conocimientos de la mascota para decifrar la fecha. Una vez que hayan resuelto el acertijo, utilicen la fecha como contraseña para desbloquear un archivo secreto. 
    Dentro del archivo, encontrarán pistas que las guiarán hacia el artilugio mágico escondido.
    
    Recuerden trabajar juntas y apoyarse mutuamente en esta aventura. 
    ¡Que la magia las acompañe!
    
    """
    pdf_1 = 'static/artilugio1_pss.pdf'  # Ruta del archivo PDF protegido con contraseña
    pdf_2 = 'static/artilugio2_pss.pdf'  # Ruta del archivo PDF protegido con contraseña

    # Crear mensaje multipart
    msg_1 = MIMEMultipart()
    msg_1['From'] = from_address
    msg_1['To'] = to_address_1
    msg_1['Subject'] = 'Cumpleaños Isabella 2023'

    # Agregar cuerpo del mensaje
    msg_1.attach(MIMEText(message_1, 'plain'))

    # Agregar archivo adjunto
    with open(pdf_1, 'rb') as pdf:
        attach = MIMEApplication(pdf.read(), _subtype='pdf')
        attach.add_header('Content-Disposition', 'attachment', filename='archivo.pdf')
        msg_1.attach(attach)

    # Crear mensaje multipart
    msg_2 = MIMEMultipart()
    msg_2['From'] = from_address
    msg_2['To'] = to_address_1
    msg_2['Subject'] = 'Cumpleaños Isabella 2023'

    # Agregar cuerpo del mensaje
    msg_2.attach(MIMEText(message_2, 'plain'))

    # Agregar archivo adjunto
    with open(pdf_2, 'rb') as pdf:
        attach = MIMEApplication(pdf.read(), _subtype='pdf')
        attach.add_header('Content-Disposition', 'attachment', filename='archivo.pdf')
        msg_2.attach(attach)

    try:
        # Configurar el servidor SMTP
        smtp_server = 'smtp.office365.com'
        port = 587

        # Conectar y enviar correo electrónico
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address_1, msg_1.as_string())
        server.sendmail(from_address, to_address_2, msg_2.as_string())
        server.quit()

        print(f'Correo enviado correctamente a {to_address_1}')
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

    message_sent = 'El correo ha sido enviado a los estudiantes. ' \
                   'Debes contactarlos para ver su contenido, quizás tengan que ver la bandeja de spawn.'

    return render_template('send_email.html', message_sent=message_sent)


@app.route('/find_gifts', methods=['POST'])
def find_gifts():
    return render_template('find_gifts.html')


@app.route('/redirigir', methods=['POST'])
def redirigir():
    texto = request.form['texto'].lower()
    if texto == 'relojiu temporis':
        return redirect('/now')
    elif texto == '06052009':
        return redirect('/luna')
    elif texto == 'az866825':
        return redirect('/viaje')
    else:
        return redirect('/error')

@app.route('/now')
def sol():
    return render_template('now.html')


@app.route('/luna')
def luna():
    return render_template('luna.html')


@app.route('/viaje')
def viaje():
    return render_template('viaje.html')


@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/call_function1', methods=['GET'])
def call_function1():
    result = dar_hora()
    return result

def dar_hora():
    # Ejecutar el script Python ubicado en otra ubicación usando Popen
    process = subprocess.Popen(["python", script_path], cwd=script_directory)
    # Esperar algunos segundos (puedes ajustar este tiempo según lo necesites)
    time.sleep(300)
    # Detener el subproceso
    process.terminate()
    return None


@app.route('/call_function2', methods=['GET'])
def call_function2():
    result = pista_biblioteca()
    return result

def pista_biblioteca():
    ciclo = 1
    while ciclo < 70:
        now = datetime.now()
        minutes = now.minute

        if minutes % 10 == 0:
            process = subprocess.Popen(["python", script_path_2], cwd=script_directory)
            time.sleep(60)
            process.terminate()
        time.sleep(10)
        ciclo += 1
    return None


@app.route('/call_function3', methods=['GET'])
def call_function3():
    result = pista_pasaporte()
    return result

def pista_pasaporte():
    ciclo = 1
    while ciclo < 70:
        now = datetime.now()
        minutes = now.minute

        if minutes % 1 == 0:
            process = subprocess.Popen(["python", script_path_3], cwd=script_directory)
            time.sleep(60)
            process.terminate()
        time.sleep(10)
        ciclo += 1
    return None


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)