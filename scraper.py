import requests
from transformers import pipeline
import gspread
from google.oauth2.service_account import Credentials
import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# NewsAPI Configuration
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

NEWS_API_URL = 'https://newsapi.org/v2/everything'

# Google Sheets Configuration
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 
'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'credentials.json'
SHEET_NAME = 'Avocado news scrapper'

# Initialize Google Sheets API
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)
sheet = client.open(SHEET_NAME).sheet1

# Summarizer setup using Hugging Face transformers
summarizer = pipeline('summarization')

# def fetch_news(query='debate'):
#     """Fetches news from NewsAPI."""
#     try:
#         today = datetime.date.today()
#         params = {
#             'q': query,
#             'from': today.strftime('%Y-%m-%d'),
#             'to': today.strftime('%Y-%m-%d'),
#             'apiKey': NEWS_API_KEY,
#             'language': 'en',
#             'pageSize': 5
#         }
#         response = requests.get(NEWS_API_URL, params=params)
#         response.raise_for_status()  # Raise an error for bad status codes
#         news_data = response.json()
#         return news_data['articles'] if 'articles' in news_data else []
#     except requests.RequestException as e:
#         print(f"Request failed: {e}")
#         return []

def fetch_news(query):
    """Fetches news from NewsAPI."""
    try:
        params = {
            'q': query,
            'from': '2024-09-01',
            'to': '2024-09-13',
            'apiKey': NEWS_API_KEY,
            'language': 'en',
            'pageSize': 5
        }
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        news_data = response.json()
        return news_data['articles'] if 'articles' in news_data else []
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

def summarize_article(content):
    """Summarizes the given article using a text summarization model."""
    if content:  # Ensure content is not empty
        summary = summarizer(content, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    return 'No Summary Available'

def save_to_google_sheets(news_data):
    """Saves news data to Google Sheets."""
    for news in news_data:
        date = news.get('publishedAt', 'No Date')
        title = news.get('title', 'No Title')
        author = news.get('author', 'No Author')
        content = news.get('content', 'No Content')
        url = news.get('url', 'No URL')
        summary = summarize_article(content)
        
        # Append to Google Sheet
        sheet.append_row([date, title, author, content, summary, url])
        print(f"Saved article: {title}")  # Debugging line

def search_news(query='farming africa'):
    """Fetches and summarizes news articles, then saves them to Google Sheets."""
    articles = fetch_news(query)
    print(f"Fetched {len(articles)} articles")  # Debugging line
    
    if articles:
        save_to_google_sheets(articles)
        print(f"Updated Google Sheet with {len(articles)} articles.")
    else:
        print("No articles to update.")

if __name__ == "__main__":
    search_news()
