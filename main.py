from datetime import *
import datetime

def calc_date(start):
    today_date = date.today()
    four_weeks = datetime.timedelta(weeks = 4)
    while today_date > start:
        start = start + four_weeks
    if today_date < start:
        start = start - datetime.timedelta(days = 1)    
    return start 


d1, m1, y1 = [int(x) for x in input("What is the start date of the contract? (DD-MM-YYYY please): ").split('-')]
start_date = date(y1, m1, d1)

print(calc_date(start_date))