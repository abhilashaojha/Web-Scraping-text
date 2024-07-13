# Web Scraping for Text

This project is a web scraper that extracts article titles and content from a list of URLs provided in a Google Sheet. The extracted articles are saved as text files with the URL ID as the filename.

## Table of Contents

* Introduction
* Features
* Prerequisites
* Installation
* Usage
* File Structure
* Error Handling
* Contributing
* License

## Introduction

This project demonstrates how to use Python to scrape web content and save it locally. It leverages the `gspread` library to interact with Google Sheets and the `BeautifulSoup` library to parse HTML content. The URLs to be scraped are listed in a Google Sheet, link of the same is available below given by BlackCoffer: 

`https://docs.google.com/spreadsheets/d/1D7QkDHxUSKnQhR--q0BAwKMxQlUyoJTQ/edit?gid=823090326#gid=823090326`


## Features

* Reads URLs from a Google Sheet.
* Extracts article titles and content.
* Saves the extracted content as text files.
* Handles request errors and missing HTML elements gracefully.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3.11.7 or higher
* A Google Cloud Platform project with the Google Sheets API enabled.
* A service account with access to the Google Sheet.
* The `json` file for authentication.

<!-- ! how to get the json key from GCC???? --- ADDDDDD a file/link/steps for that -->

## Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Web-Scraping-text.git
cd web-scraper
```

#### 2. Update Configuration Files

* Ensure that you replace the placeholder paths and filenames in the code with the appropriate paths to your own Google Cloud Credentials JSON key file. This will enable authenticated access to the Google Sheets API.

#### 3. Install Dependencies

```bash

pip install -r requirements.txt
```

## Usage

#### 1. Share the Google Sheet with the Service Account

* Open your Google Sheet.
* Click the "Share" button.
* Add the email address of your service account (found in the credential json file) with "Viewer" access.

#### 2. Update the Script with Your JSON Key File Path

Ensure the path to your JSON key file is correctly set in the script:
```bash
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/json/file", scope)
```

#### 3. Run the Script
```bash
python web_scraper.py
```
The script will read the URLs from the Google Sheet, scrape the content, and save it in the articles directory.

<!-- ## File Structure

web-scraper/ 
│
├── articles/                      # Directory where the scraped articles will be saved
│   ├── <URL_ID_1>.txt
│   ├── <URL_ID_2>.txt
│   └── ...
│
├── requirements.txt               # List of required Python packages
├── certain-density-411209-233e2fd7eb18.json  # Service account credentials (not included in the repository)
├── web_scraper.py                 # The main script for web scraping
└── README.md                      # This README file -->

## Error Handling
The script includes basic error handling:

* If a request to fetch the URL fails, an error message is printed, and the script continues with the next URL.

* If the title or content of the article is not found, the script substitutes with "No Title Found" or skips content extraction respectively.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

--- 

By following the instructions in this README, you should be able to set up and run the web scraper successfully. If you encounter any issues or have suggestions for improvement, please feel free to contribute or raise an issue on GitHub.

### Future Works

Performing Textual Analysis on the extracted article and find out different metrics related to the article.

Furthermore, to add steps for creating GCC account and json keys. 