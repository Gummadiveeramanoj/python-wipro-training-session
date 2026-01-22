import requests
from bs4 import BeautifulSoup
import json

# 1. Fetch the HTML webpage
url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
response = requests.get(url)

# Check if request is successful
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to fetch webpage")
    exit()

# 2. Parse HTML using BeautifulSoup with lxml parser
soup = BeautifulSoup(html_content, "lxml")

# 3. Extract required data

# a) Page Title
page_title = soup.title.text if soup.title else "No title found"

# b) All hyperlinks
links = []
for a_tag in soup.find_all("a"):
    link_text = a_tag.text.strip()
    link_href = a_tag.get("href")
    links.append({
        "text": link_text,
        "url": link_href
    })

# c) Specific list data (example: <ul> or <ol>)
list_items = []
for li in soup.find_all("li"):
    list_items.append(li.text.strip())

# 4. Convert extracted data into JSON format
extracted_data = {
    "page_title": page_title,
    "hyperlinks": links,
    "list_items": list_items
}

# 5. Save output into a JSON file
with open("extracted_data.json", "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print("Data extracted and saved successfully!")
