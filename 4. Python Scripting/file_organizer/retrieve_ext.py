from bs4 import BeautifulSoup
import requests
import json

# Wrote this to scrape from a website I found useful to categorize each extension into a json for my main to read.

url = "https://www.computerhope.com/issues/ch001789.htm"

response =requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# create a list of categories, last h2 is "related information" which is not relevant
categories = [i.getText().split("file")[0] for i in soup.find_all("h2")][:-1]

# create a list of ul, first 2 and last 4 info is not relevant
unformat_lists = soup.find_all("ul")[2:-4]

# create a list to store all information retrieve
extensions = []
for ul in unformat_lists:
    cat_list = [li.find("b").getText() for li in ul.find_all("li")]
    extensions.append(cat_list)

# create a dictionary to house
extension_categories = {}
for i in range(len(categories)):
    extension_categories[categories[i].strip()] = extensions[i]

json_object = json.dumps(extension_categories, indent=4)

with open("extension_categories.json", "w") as data:
    data.write(json_object)