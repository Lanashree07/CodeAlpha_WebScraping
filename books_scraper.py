import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "http://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Store data
data = []

# Extract details
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save data to CSV file
df.to_csv("books_data.csv", index=False)

print("Data saved successfully!")
print(df.head())