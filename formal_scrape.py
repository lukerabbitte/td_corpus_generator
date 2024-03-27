import requests
from bs4 import BeautifulSoup

def scrape_and_write_to_file(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Open a text file to write the body text of the articles
        with open(filename, "a", encoding="utf-8") as f:
            # Find all article links
            article_links = soup.find_all("a", class_="link-overlay-redesign")

            # Iterate over each article link
            for link in article_links:
                # print(f"link worked: {link}")
                # Send a GET request to the article URL
                article_response = requests.get(link['href'])

                if article_response.status_code == 200:
                    # Parse the HTML content of the article
                    article_soup = BeautifulSoup(article_response.content, "html.parser")

                    # Find the div containing the body text of the article
                    body_div = article_soup.find("div", class_="article-content-redesign")

                    if body_div is not None:
                        # Find all p tags within the body div
                        paragraphs = body_div.find_all("p")

                        # Extract the text from each p tag and write it to the file
                        for p in paragraphs:
                            p_text = p.get_text(strip=True)
                            # print(f"paragraph (p) text: {p_text}")

                            # Check if the paragraph text starts with the unwanted phrases
                            if not p_text.startswith("With additional reporting by") and not p_text.startswith("Making a difference") and not p_text.startswith("Advertisement") and not p_text.startswith("Subscribe") and not p_text.startswith("Whoops") and not p_text.startswith("For the price of") and not p_text.startswith("TheJournal"):
                                # Write the body text to the file, followed by a newline character
                                f.write(p_text + "\n")

        print("Articles scraped successfully and saved to", filename)
    else:
        print("Failed to retrieve the page:", response.status_code)

# Call the function with the URL and the filename for the text file
for page_number in range(1, 6):  # 6 is exclusive, so it will loop through pages 1 to 5
    if page_number == 1:
        url = "https://www.thejournal.ie/enda-kenny/news/"
    else:
        url = f"https://www.thejournal.ie/enda-kenny/news/page/{page_number}/"
    scrape_and_write_to_file(url, "formal-articles.txt")