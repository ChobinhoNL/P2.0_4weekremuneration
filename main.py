from datetime import *
import datetime
from flask import Flask, request, render_template



app = Flask(__name__)

def calc_date(start):
    today_date = date.today()
    four_weeks = datetime.timedelta(weeks = 4)
    while today_date > start:
        start = start + four_weeks
    if today_date <= start:
        start = start - datetime.timedelta(days = 1)
    last_day = f"{start.day}-{start.month}-{start.year}"
    return last_day 

@app.route('/', methods =["GET", "POST"])
def start():
    # start = request.args['date']
    # d1, m1, y1 = [int(x) for x in start("Wat is de startdatum van het contract? (DD-MM-YYYY please): ").split('-')]
    if request.method == "POST":
        start = request.form.get("startdate")
        d1 = int(f"{start[0]}{start[1]}")
        m1 = int(f"{start[3]}{start[4]}")
        y1 = int(f"{start[6:]}")
        start_date = date(y1, m1, d1)
        result = str(calc_date(start_date))
        return render_template("response.html", value=result) 

    return render_template("form.html")

if __name__=='__main__':
   app.run()