import datetime
from copyfromclipboard import getClipboardText

# get current date time
def current_date_time():
    date = datetime.datetime.now()
    date = str(date)
    date = date.split(" ")
    date = date[0]
    return date

def createHeading():
    # Heading
    print('Tags: ')
    print('Software: ')
    print('Link: ' + getClipboardText())
    print('Created on: ' + current_date_time())
    print('___________________________________')
    print('# Heading')
    print('*About the project*')


createHeading()
