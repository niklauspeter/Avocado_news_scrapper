import gspread
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

# Load credentials from the downloaded JSON file
credentials = Credentials.from_service_account_file('avocado-web-scrapper-4408c53fe3a9.json', scopes=SCOPES)

# Authorize the gspread client
client = gspread.authorize(credentials)

# Open the Google Sheet by name
sheet = client.open('Avocado news scrapper').sheet1

# Example: Add a test row to verify access
sheet.append_row(['Test', 'Connection', 'Successful'])

