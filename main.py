import datetime as dt
import pandas
import random
import smtplib

USERNAME = "test@example.com"
PASSWORD = "examplepassword"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row.month ,data_row.day): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    random_letter = random.randint(1,3)
    print(random_letter)

    with open(f'letter_templates/letter_{random_letter}.txt', 'r') as file:
        letter = file.read()
        changed_letter = letter.replace("[NAME]", "Dorian")

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs=birthdays_dict[today].email,
                            msg=f"Subject:Happy Birthday\n\n{changed_letter}")
