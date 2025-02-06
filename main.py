# import smtplib
#
# my_email = "abecadlo@gmail.com"
# password = "venxft233asdv"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="testing@yahoo.com", msg="Subject: Testing\n\nThis is testing message.")

import datetime as dt

date = dt.datetime.now()
year = date.tzinfo
# print(year)

date_of_birth = dt.datetime(year=1990, month=1, day=22)
print(date_of_birth)

