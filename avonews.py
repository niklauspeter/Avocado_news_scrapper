import requests
import datetime
import gspread
from google.oauth2.service_account import Credentials
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# NewsAPI Configuration
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = 'https://newsapi.org/v2/everything'

# Google Sheets Configuration
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = 'credentials.json'
# SHEET_ID = 'Avocado news scrapper'

# Summarization Model
summarizer = pipeline("summarization")

# Initialize Google Sheets API
creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open('Avocado news scrapper').sheet1

def fetch_news():
    """Fetches avocado-related news from NewsAPI."""
    today = datetime.date.today()
    params = {
        'q': 'debate',
        'from': today.strftime('%Y-%m-%d'),
        'to': today.strftime('%Y-%m-%d'),
        'apiKey': NEWS_API_KEY,
        'language': 'en',
        'pageSize': 5
    }
    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()
    return news_data['articles'] if 'articles' in news_data else []

def summarize_article(article):
    """Summarizes the given article using a text summarization model."""
    summary = summarizer(article['content'], max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def update_google_sheet(date, summaries):
    """Updates the Google Sheet with summarized news articles."""
    row = [date] + summaries
    sheet.append_row(row)

def main():
    today = datetime.date.today().strftime('%Y-%m-%d')
    articles = fetch_news()
    
    if articles:
        summaries = []
        for article in articles:
            try:
                summary = summarize_article(article)
                summaries.append(summary)
            except Exception as e:
                print(f"Failed to summarize article: {e}")
        
        update_google_sheet(today, summaries)
        print(f"Updated Google Sheet with {len(summaries)} articles for {today}.")
    else:
        update_google_sheet(today, ['No news articles found','No news articles found'])
        print("No news articles found.")

if __name__ == "__main__":
    main()
