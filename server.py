from flask import *
import urllib.parse
from datetime import datetime
app = Flask(__name__)
year = str(datetime.now().year)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/love', methods=['GET'])
def lovely():
    lover = request.args.get('lover', 'Valentine')
    host = request.args.get('host', 'Enitnelav')
    return render_template('lovely.html', lover=lover, host=host)

@app.route('/day', methods=['GET'])
def get_valentines_message():
    # Get the date from the query parameter
    date_str = request.args.get('date')
    lover = request.args.get('lover', 'Valentine')
    valentines_week = {
    year + "-" + "02-07": "Happy Rose Day " + lover + "!" + " 🌹 Share a beautiful rose with your loved one.",
    year + "-" + "02-08": "Happy Propose Day " + lover + "!" + " 💍 Confess your love and make it special.",
    year + "-" + "02-09": "Happy Chocolate Day " + lover + "!" + " 🍫 Sweeten the day with some chocolate treats.",
    year + "-" + "02-10": "Happy Teddy Day " + lover + "!" + " 🧸 Share a cute teddy to make them smile.",
    year + "-" + "02-11": "Happy Promise Day " + lover + "!" + " 🤝 Make promises to cherish each other forever.",
    year + "-" + "02-12": "Happy Hug Day " + lover + "!" + " 🤗 A warm hug to show your love.",
    year + "-" + "02-13": "Happy Kiss Day " + lover + "!" + " 💋 Seal your love with a kiss.",
    year + "-" + "02-14": "Happy Valentine's Day " + lover + "!" + " ❤️ Celebrate your love and make memories!"
    }
    try:
        # Validate the date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # Check if the date is in Valentine's week
        if date_str in valentines_week:
            message = valentines_week[date_str]
        else:
            # If it's not Valentine's week, return a general love letter
            message = (
                "Love knows no calendar. You are loved every day, and today is no exception. "
                "Take a moment to appreciate the beauty of life and those who make it worthwhile. 💖"
            )
        return jsonify({"message": message})
    except (ValueError, TypeError):
        return jsonify({"message": "Invalid date format. Please provide a valid date in YYYY-MM-DD format."}), 400

if __name__ == "__main__":
    app.run(debug=False)
