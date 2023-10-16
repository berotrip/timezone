from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    time_zones = ['America/Los_Angeles', 'America/New_York', 'America/Chicago', 'America/Denver', 'Europe/London', 'Europe/Paris', 'Asia/Tokyo', 'Asia/Kolkata', 'Australia/Sydney', 'Pacific/Auckland']
    time_data = []
    for tz in time_zones:
        current_time = datetime.now(pytz.timezone(tz))
        time_data.append({'time_zone': tz, 'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S')})
    return render_template('home.html', time_data=time_data)

if __name__ == "__main__":
    app.run(debug=True)
