import time

from bs4 import BeautifulSoup
from rich import print
from selenium import webdriver


def currency_converter(search_term: str) -> str:
    """
    Converts from one currency to another
    :param search_term: i.e. "1 USD to EUR"
    :return: str
    """
    url = "https://www.google.com/search?q={}".format(
        "+".join(search_term.split())
    )

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.add_argument("--user-agent={}".format(user_agent))
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Get the value of the converted currency
    from_value = soup.find("div", {"class": "vk_sh c8Zgcf"})
    to_value = soup.find("div", {"class": "dDoNo ikb4Bb gsrt"})

    if from_value and to_value:
        return f"{from_value.text} {to_value.text}"
    return "Could not convert currency"


if __name__ == "__main__":
    print("Enter your search term:")
    st = input()
    print(currency_converter(st))
