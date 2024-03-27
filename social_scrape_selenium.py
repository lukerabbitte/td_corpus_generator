from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_and_write_to_file(url, filename):
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # Go to the page
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))

    # Parse the HTML content of the page
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Open a text file to write the body text of the articles
    with open(filename, "a", encoding="utf-8") as f:
        # Find all article links
        article_links = soup.find_all("a", class_="link-overlay-redesign")

        # Iterate over each article link
        for link in article_links:
            print(f"link worked: {link['href']}")
            # Go to the article URL
            driver.get(link['href'])

            # Wait for the page to load
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))

            # Parse the HTML content of the article
            article_soup = BeautifulSoup(driver.page_source, "html.parser")

            comments = article_soup.find_all("div", class_="comment-body text")

            for c in comments:
                comment_text = c.get_text(strip=True)
                print(comment_text)
                f.write(comment_text + "\n")

    print("Articles scraped successfully and saved to", filename)

    # Don't forget to close the driver
    driver.quit()

# Call the function with the URL and the filename for the text file
for page_number in range(1, 6):  # 6 is exclusive, so it will loop through pages 1 to 5
    if page_number == 1:
        url = "https://www.thejournal.ie/enda-kenny/news/"
    else:
        url = f"https://www.thejournal.ie/enda-kenny/news/page/{page_number}/"
    scrape_and_write_to_file(url, "social-comments.txt")