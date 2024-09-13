# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import search_news

def start_scheduler():
    """Starts the scheduler to run `search_news` immediately and then every 24 hours."""
    scheduler = BackgroundScheduler()
    
    # Run the search_news function immediately
    search_news()
    
    # Schedule to run `search_news` every 24 hours
    scheduler.add_job(search_news, 'interval', hours=24)
    
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()
