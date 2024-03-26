from datetime import datetime
import pandas
import random
import smtplib

my_email = ""
my_password = ""

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("day32\\birthday_wisher\\birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"day32\\birthday_wisher\\letter_templates\\letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=(birthday_person["email"]), msg=f"Subject:Happy Birthday!\n\n {contents}")
    