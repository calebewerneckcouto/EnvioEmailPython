import smtplib
from email.mime.text import MIMEText

def enviar_email_smtp():
    # Configurações do email
    assunto = "Assunto do Email"
    corpo = "Este é o corpo da mensagem"
    remetente = "calebewerneck@gmail.com"
    destinatarios = ["calebewerneck@yahoo.com", "calebewerneck@hotmail.com"]
    senha = ""
    
    # Configurações do servidor
    servidor_smtp = 'smtp.gmail.com'
    porta = 587
    ssl = False
    tls = True
    
    try:
        # Conectar ao servidor
        with smtplib.SMTP(servidor_smtp, porta) as smtp_server:
            # Configurar TLS
            if tls:
                smtp_server.starttls()
            
            # Login no servidor
            smtp_server.login(remetente, senha)
            
            # Criar mensagem para cada destinatário
            for destinatario in destinatarios:
                msg = MIMEText(corpo)
                msg['Subject'] = assunto
                msg['From'] = remetente
                msg['To'] = destinatario
                msg['Reply-To'] = remetente  # Adicionado para melhor rastreabilidade
                msg['X-Mailer'] = 'Python SMTP'  # Identificador do software
                
                try:
                    # Enviar email
                    smtp_server.sendmail(remetente, destinatario, msg.as_string())
                    print(f"Email enviado com sucesso para {destinatario}!")
                except smtplib.SMTPException as e:
                    print(f"Erro ao enviar email para {destinatario}: {e}")
    
    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação. Verifique sua senha de aplicativo.")
    except smtplib.SMTPException as e:
        print(f"Erro ao conectar ao servidor SMTP: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Execute a função
enviar_email_smtp()