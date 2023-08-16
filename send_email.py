import smtplib
USERNAME = 'pythonforsuccess@gmail.com'
PASSWORD = 'pvnamgpuyqbzrito'


class SendEmail:
    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs='abalakas777@gmail.com',
                msg=f'Subject: Message From Portfolio Website \n\n'
                    f'Sender Name: {self.name}\n'
                    f'Sender Phone Number: {self.phone}\n'
                    f'Sender Email: {self.email}\n'
                    f'Message: {self.message}'
            )
