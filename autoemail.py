#!/usr/bin/env python3

import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(
        self,
        email,
        parola,
        catre = "abator@avicolafocsani.com",
        subiect = "Comanda magazin abator"
    ):
        self.email = email
        self.parola = parola
        self.catre = catre
        self.subiect = subiect

        self.MESAJ = MIMEMultipart('mesaj')

    def sendEmail(self) -> bool:
        if self.MESAJ != 'None':
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            server.starttls()
            server.login(self.email, self.parola)
            server.sendmail(self.email, self.catre, msg=self.MESAJ)
            server.quit()
        # else:
            #     print("\nemail-ul nu a fost trimis")
            #     return False
            # print("email trimis")
            # return True

    def  createMessage(self)-> str:
        self.MESAJ['Subject'] = self.subiect
        self.MESAJ['From'] = self.email
        self.MESAJ['To'] = self.catre
        mesaj = "Refrigerate\n\n"
        produse = [
            "Pui griller pg",
            "Piept dezosat fara piele pg",
            "Aripi pg",
            "Piept cu os pg",
            "Pulpa dezosata cu piele pg",
            "Ficat tv",
            "Pipote tv",
            "Pulpa intreaga tv",
            "Pulpa superioara tv",
            "Pulpa inferioara tv",
            "Aripi tv",
            "Carne tocata tv",
            "Mici formati tv",
            "Carnati pasare tv",
            "Pulpa intreaga vrac",
            "Pulpa superioara vrac",
            "Spinari cu aripa vrac"
        ]
        for produs in produse:
            addProd = input(f"Adaugati {produs}? [d/n]")
            if addProd.lower() == "d" or addProd.lower() == "da":
                kg = input(f"Cate kg de {produs}?")
                mesaj += f"{produs} {kg} kg\n"
            elif addProd.lower() == "gata":
                break
        mesaj = MIMEText(mesaj)
        self.MESAJ.attach(mesaj)
        return mesaj


if __name__ == "__main__":
    emailUser = input('Email:')
    password = getpass()
    email = Email(emailUser, password, catre="camioane112@gmail.com")
    email.createMessage()
    email.sendEmail()