import gspread
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from oauth2client.service_account import ServiceAccountCredentials

def fetch_and_save_article(url, url_id, output_dir):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article title
        title_tag = soup.find('h1', class_='entry-title')  # Adjust class or id if necessary
        title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'

        # Extract the article content
        content_div = soup.find('div', class_='td-post-content')  # Adjust class or id if necessary
        paragraphs = content_div.find_all('p') if content_div else []
        article_text = '\n'.join([p.get_text(strip=True) for p in paragraphs])

        # Combine title and article text
        full_text = f"{title}\n\n{article_text}"

        # Save to a text file with URL_ID as the file name
        file_path = os.path.join(output_dir, f"{url_id}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(full_text)
        print(f"Article {url_id} saved successfully.")
    except Exception as e:
        print(f"Failed to fetch or save article {url_id}: {e}")

def main():
    # Define the scope and authenticate the service account
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credential/json/file", scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet by URL
    # The URL was given by Blackcoffer

    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1Y6Y1OisSJsFjc7Wf4TNV3xCbJMdtiXXN0WXOG_pbsAE/edit?usp=sharing')
    worksheet = sheet.get_worksheet(0)  # Use the first sheet

    # Get all values in the worksheet
    data = worksheet.get_all_records()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Ensure the output directory exists
    output_dir = 'articles'
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each row and fetch the article
    for _, row in df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        fetch_and_save_article(url, url_id, output_dir)

if __name__ == "__main__":
    main()
