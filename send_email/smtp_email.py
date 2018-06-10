from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = 'smtp.gmail.com'
port = 540
username = "iamadrianachen@gmail.com"
password = "s2yF!pAaOGGjYY^%!Zx62Mp"
from_email = username
to_list = ["venusgrape17@gmail.com"]



def main():
    
  try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)

    the_msg = MIMEMultipart('alternative')
    the_msg['Subject'] = 'hello there'
    the_msg['From'] = from_email
    # the_msg['To'] = to_list[0]
    plain_txt = 'Testing email message'
    html_txt = """
        <b>hieelo</b>
        """

    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')
    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
  except smtplib.SMTPException:
    print('error sending')
  


if __name__ == '__main__':
  main()
  print('runing')