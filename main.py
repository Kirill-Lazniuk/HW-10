import pandas as pd
import datetime
import time
import yagmail
from news import NewsFeed
import config


last_sent_date = None

def send_emails():
    df =pd.read_excel("people.xlsx")
    yag = yagmail.SMTP(user="your_email@gmail.com", password="your_app_password")

    for index, row in df.iterrows():
        user_interest = row['interest']
        user_lang = row['language'] 
        
        news_feed = NewsFeed(interest=user_interest, language=user_lang)
        email_body = news_feed.get_news() 
        
        mail_contents = f"Hi {row['name']}\n\n See what's on about {user_interest} today!\n\n {email_body}"
        
        yag.send(to=row['email'], subject=f"Your {user_interest} news", contents=mail_contents)
    print("Всі листи відправлено.")


while True:
    now = datetime.datetime.now()
    today_date = now.date()

    if now.hour >= config.TARGET_HOUR and now.minute >= config.TARGET_MINUTE:
        if last_sent_date != today_date:
            send_emails()
            last_sent_date = today_date
    
    time.sleep(60)