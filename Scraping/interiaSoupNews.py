from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.interia.pl/').text
soup = BeautifulSoup(html_text, 'lxml')

# Parsing the headlines of the main articles
main_interia_news = soup.find_all('li', class_ = 'wiadspec-li tile-half tile')
other_headlines = soup.find_all('li', class_ = 'wiadspec-li tile tile-standard' )

counter = 1 # This is a counter for each of the articles


print("----- INTERIA NEWS ------")


def extract_title_and_link(parameter): #
    """extract the title and a link."""
    a = parameter.find("a")
    if not a:
        return None, None

    title = a.get_text(" ", strip=True)
    link = a.get("href")

    return title, link


for news in main_interia_news:
    title, link = extract_title_and_link(news)
    print(f"{counter}. {title}")
    print(f"   {link}")
    counter += 1

for headlines in other_headlines:
    title, link = extract_title_and_link(headlines)
    print(f"{counter}. {title}")
    print(f"   {link}")
    counter += 1
