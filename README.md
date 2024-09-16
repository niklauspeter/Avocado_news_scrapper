# Avocado News Scraper

Avocado News Scraper is a Python application that fetches news articles on avocados(or any query you hardcode) from the NewsAPI based on specific queries, summarizes them using a natural language processing model, and saves the results to a Google Sheets document. This app is particularly useful for gathering up-to-date information on specific topics and storing them in a structured format for further analysis.

## Features

- Fetches news articles using the NewsAPI.
- Summarizes the content of news articles using a pre-trained model from Hugging Face.
- Saves news details, including the title, author, publication date, content, summary, and URL, to a Google Sheet.

## Technologies Used

- Python
- NewsAPI
- Hugging Face Transformers
- Google Sheets API (`gspread`)
- Google OAuth2 (`google-auth`)
- `requests` library

## Prerequisites

- Python 3.8 or higher
- NewsAPI Key (get it from [NewsAPI](https://newsapi.org/))
- Google Cloud service account credentials for Google Sheets API access
- Required Python libraries (listed in `requirements.txt`)

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/avocado-news-scraper.git
   cd avocado-news-scraper
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add your API keys:
   ```plaintext
   NEWS_API_KEY=your_news_api_key
   GOOGLE_SHEETS_CREDENTIALS=credentials.json
   ```

5. **Google Sheets Configuration**:
   - Create a Google Cloud service account and enable the Google Sheets API.
   - Download the service account credentials file (`credentials.json`) and place it in the project directory.
   - Share the target Google Sheet with the service account email address.

6. **Add Sensitive Files to `.gitignore`**:
   Ensure that sensitive files such as `credentials.json` and `.env` are listed in your `.gitignore` file to prevent accidental exposure.

## Usage

1. **Run the App**:
   To fetch, summarize, and save news articles, run the following command:
   ```bash
   python3 scraper.py #adjust to your python version
   ```

2. **Customize the Query**:
   You can change the query parameter in the `search_news()` function to fetch articles on different topics:
   ```python
   search_news(query='technology')
   ```

## Example Output

- The fetched articles will be summarized and saved in the specified Google Sheets document. The spreadsheet will include columns for the date, title, author, content, summary, and URL of each article.

## Troubleshooting

- Ensure that your API keys are correctly set and that your service account has access to the Google Sheets.
- Check that the NewsAPI quota has not been exceeded.
## Contributors
- niklauspeter - backend engineer
-fabiannyongesa - script and product ideation

## Contributing

If you wish to contribute to this project, please fork the repository and create a pull request. Ensure your code follows the PEP 8 guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NewsAPI](https://newsapi.org/) for providing the news data.
- [Hugging Face](https://huggingface.co/) for the summarization model.
- [Google Cloud](https://cloud.google.com/) for the Sheets API.
```

### Key Points Explained

- **Project Overview**: Briefly explains what the app does.
- **Setup Instructions**: Guides the user on how to clone, set up the environment, and install dependencies.
- **Usage**: Shows how to run the script and change the query parameters.
- **Contributing**: Encourages contributions and provides basic guidelines.
- **Acknowledgments**: Credits the main technologies and services used in the app.
