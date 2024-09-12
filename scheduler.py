# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import search_news

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(search_news, 'interval', hours=24)  # Run daily
    scheduler.start()
