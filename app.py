# app.py
from flask import Flask
from scheduler import start_scheduler

app = Flask(__name__)

@app.route('/')
def home():
    return "Avocado News Scraper is running!"

if __name__ == '__main__':
    # Start the scheduler when the Flask app starts
    start_scheduler()
    app.run(debug=True)
