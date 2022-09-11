import smtplib
import datetime as dt
import random

def email_sender():
    my_email = "@mail"
    password= "passwords"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="@tomail",
            msg=f"Subject:Hello\n\n{random_quote}".encode("utf8")
        )

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt", mode="r", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    email_sender()


