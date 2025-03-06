# Envio de E-mails via SMTP com Python

Este script em Python envia e-mails para múltiplos destinatários usando o servidor SMTP do Gmail. Ele utiliza a biblioteca `smtplib` para se conectar ao servidor de e-mail e `email.mime.text.MIMEText` para formatar a mensagem.

## Requisitos

Para executar este script, é necessário ter o Python instalado em sua máquina. Também será necessário um acesso a uma conta do Gmail e a criação de uma senha de aplicativo para autenticação (caso a autenticação de dois fatores esteja ativada).

Além disso, o script usa a biblioteca `smtplib`, que já vem com o Python, e a biblioteca `email.mime.text` para criar o e-mail.

## Como usar

1. **Configuração do Gmail:**
   - Se você estiver usando autenticação de dois fatores em sua conta do Gmail, crie uma senha de aplicativo [aqui](https://myaccount.google.com/apppasswords).
   - Caso contrário, você pode usar sua senha normal (não recomendado).

2. **Alteração do script:**
   - Substitua os valores das variáveis `remetente` e `senha` com suas informações de login.
   - Altere o `assunto` e o `corpo` da mensagem conforme necessário.
   - Adicione ou remova destinatários da lista `destinatarios`.

3. **Executando o script:**
   - Execute o script Python com o seguinte comando no terminal:
   ```bash
   python enviar_email_smtp.py
