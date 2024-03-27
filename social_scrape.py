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
                print(f"link worked: {link}")
                # Send a GET request to the article URL
                article_response = requests.get(link['href'])
                # print(f"article_response: {article_response}")

                if article_response.status_code == 200:
                    # Parse the HTML content of the article
                    article_soup = BeautifulSoup(article_response.content, "html.parser")
                    # with open("tmp.txt", "w", encoding="utf-8") as f:
                    #     f.write(article_soup.prettify())

                    comments = article_soup.find_all("div", class_="comment-body text")

                    for c in comments:
                        comment_text = c.get_text(strip=True)
                        print(comment_text)
                        f.write(comment_text + "\n")


        print("Articles scraped successfully and saved to", filename)
    else:
        print("Failed to retrieve the page:", response.status_code)

# Call the function with the URL and the filename for the text file
for page_number in range(1, 6):  # 6 is exclusive, so it will loop through pages 1 to 5
    if page_number == 1:
        url = "https://www.thejournal.ie/enda-kenny/news/"
    else:
        url = f"https://www.thejournal.ie/enda-kenny/news/page/{page_number}/"
    scrape_and_write_to_file(url, "social-comments.txt")