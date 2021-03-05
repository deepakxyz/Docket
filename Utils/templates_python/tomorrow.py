import datetime
import sys

# Today date
def today():
    today = datetime.date.today()
    print(today)

# Tomorrow date
def tomorrow():
    today = datetime.date.today()
    today = today + datetime.timedelta(days=1)
    print(today)

# if sys.argv[0] == "today":
#     today()
# if sys.argv[0] == "tomorrow":
#     tomorrow()

if __name__ == "__main__":
    if sys.argv[1:][0] == "today":
        today()
    elif sys.argv[1:][0] == "tomorrow":
        tomorrow()