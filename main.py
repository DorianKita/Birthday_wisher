# import smtplib
import random
import datetime
import smtplib

#
my_email = "abecadlo@gmail.com"
password = "venxft233asdv"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="testing@yahoo.com", msg="Subject: Testing\n\nThis is testing message.")

with open("quotes.txt") as quotes:
    list_of_quotes = quotes.readlines()
    random_quote = random.choice(list_of_quotes)

date = datetime.datetime.now()
day = date.weekday()

if day == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="testing@yahoo.com", msg=f"Subject:Hello\n\n{random_quote}")
    print(random_quote)


