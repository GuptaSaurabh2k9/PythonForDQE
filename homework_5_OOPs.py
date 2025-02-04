'''Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.

Each new record should be added to the end of file. Commit file in git for review.
'''

# from datetime import datetime
#
# # Get user input
# user_input = input("Enter a date (YYYY-MM-DD): ")
# user_date = datetime.strptime(user_input, "%Y-%m-%d")
#
# # Get current date
# current_date = datetime.now()
#
# # Calculate difference
# difference = current_date - user_date
#
# # Display the difference
# print(f"Difference: {difference.days} days")


import datetime
# user_input = input("Enter the date in YYYY-MM-DD format ")
# user_date = datetime.datetime.strptime(user_input,"%Y-%m-%d")
# current_date = datetime.datetime.now()
# # expiration_date = datetime.datetime.now() + datetime.timedelta(days=expiration_days)
# print(user_date,current_date,(user_date-current_date).days)

# print(expiration_date)

class NewsFeed:
    def __init__(self, filename='news_feed.txt'):
        self.filename = filename
    def add_news(self, text, city):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"News | {date} | {city} | {text}\n"

    def add_advt(self, text, exp_date):
        # user_date = datetime.datetime.strptime(user_input,"%Y-%m-%d")
        current_date = datetime.datetime.now()
        exp_days = (exp_date-current_date).days
        return f"Advertisement | Days Left: {exp_days} | {city} | {text}\n"

    def add_event(self, event_detail, place):
        event_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Event | {event_date} | {place} | {event_detail}\n"

    def save_record(self, record):
        with open(self.filename, 'a') as file:
            file.write(record)
            print(f"Record added to {self.filename}")

def tool():
    news_feed = NewsFeed()

    while True:
        print("\nChoose the type of record to add:")
        print("1. News")
        print("2. Private Ad")
        print("3. Event")
        print("4. Exit")

        choice = input("Enter your choice (1-4) ")

        # text and city as input.Date is calculated during publishing.
        if choice == '1':
            city = input("Enter the City Name: ")
            text = input("Enter the News Text: ")
            record = news_feed.add_news(text, city)

        # text and expiration date as input.Day left is calculated during publishing.
        elif choice == '2':
            exp_date = input("Enter the Expiration Data in 'YYYY-MM-DD' format: ")
            text = input("Enter the Adv. Text: ")
            record = news_feed.add_advt(text, exp_date)

        elif choice == '3':
            place = input("Enter the Place of Event: ")
            event_detail = input("Enter the Event Details: ")
            record = news_feed.add_event(event_detail, place)

        elif choice == '4':
            break

        else:
            print("Enter the Valid Input")
            continue


        news_feed.save_record(record)
        break

tool()