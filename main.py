import yagmail
import pandas as pd
from news import NewsFeed
import datetime as dt
import time


def send_email():
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday.strftime('%Y-%m-%d'), to_date=today)
    email = yagmail.SMTP(user="bkinkead7@gmail.com", password="wgxeiougegvzfffx")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today.\n {news_feed.get()}")


while True:
    if dt.datetime.now().hour == 17 and dt.datetime.now().minute == 43:

        today = dt.datetime.now().strftime('%Y-%m-%d')
        yesterday = dt.datetime.now() - dt.timedelta(days=1)

        df = pd.read_excel('people.xlsx')
#print(df)
# wgxeiougegvzfffx
        for index, row in df.iterrows():
            send_email()
    time.sleep(60)