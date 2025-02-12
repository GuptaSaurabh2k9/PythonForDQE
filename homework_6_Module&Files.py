"""Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.

Each new record should be added to the end of file. Commit file in git for review.
"""

"""Expand previous Homework 5 with additional class, which allow to provide records by text file:
1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
4.Apply case normalization functionality form Homework 3/4
"""

import datetime
import os

class NewsFeed:

    def __init__(self, filename='news_feed.txt'):
        self.filename = filename

    def add_news(self, text, city):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"News | {date} | {city} | {text}\n"

    def add_advt(self, text, exp_date):
        user_date = datetime.datetime.strptime(exp_date,"%Y-%m-%d")
        current_date = datetime.datetime.now()
        exp_days = (user_date-current_date).days
        return f"Advertisement | Days Left: {exp_days} | {text}\n"

    def add_event(self, event_detail, place):
        event_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Event | {event_date} | {place} | {event_detail}\n"

    def save_record(self, record):
        with open(self.filename, 'a') as file:
            file.write(record)
            print(f"Record added to {self.filename}")

class File_process:
    def __init__(self, filename='input_feed.txt'):
        self.filename = filename

    def process_file(self):
        with open(self.filename, 'r') as f:
            records = f.readlines()
            print(records)

        news_obj = NewsFeed()

        for record in records:
            record = record.strip()
            print(record)
            if record.startswith("News"):
                parts = record.split("|")
                city = parts[1].strip()
                text = parts[2].strip()
                data = news_obj.add_news(text,city)
            elif record.startswith("Event"):
                parts = record.split("|")
                city = parts[1].strip()
                text = parts[2].strip()
                data = news_obj.add_event(text,city)
            elif record.startswith("Advertisement"):
                parts = record.split("|")
                exp_date = parts[1].strip()
                text = parts[2].strip()
                data = news_obj.add_advt(text,exp_date)
            else:
                print(f"Invalid data", record.split("|")[0])
                continue

            news_obj.save_record(data)

file_obj = File_process()

file_obj.process_file()

#####################
