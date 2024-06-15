import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(subject, html_content, to_email):
    # Configura tu cuenta de Gmail
    from_email = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASS")

    # Configuración del servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Crear el objeto del mensaje
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adjuntar el cuerpo del correo en formato HTML
    msg.attach(MIMEText(html_content, 'html'))

    # Conectarse al servidor SMTP y enviar el correo
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    # Ejemplo de uso
    subject = "Asunto del correo"
    html_content = """
    <html>
    <body>
        <h1>Hola,</h1>
        <p>Este es un correo con cuerpo en <b>HTML</b>.</p>
    </body>
    </html>
    """
    to_email = "destinatario@example.com"
    send_email(subject, html_content, to_email)
