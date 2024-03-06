import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, assunto, corpo):
    email_enviar = 'SEU EMAIL'
    senha = 'SUA SENHA'

    msg = MIMEMultipart()
    msg['From'] = email_enviar
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo, 'plain'))

    servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_smtp.starttls()
    servidor_smtp.login(email_enviar, senha)
    texto_email = msg.as_string()
    servidor_smtp.sendmail(email_enviar, destinatario, texto_email)
    servidor_smtp.quit()
