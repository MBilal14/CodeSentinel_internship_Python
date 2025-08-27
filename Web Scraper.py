# Task 4
# Write a script that: Fetches the HTML of a website
# (e.g.,https://news.ycombinator.com) Parses the HTML toextract
# all headlines Displays them as a numbered list
# 🛠 Tools: requests, BeautifulSoup, for loops
# 🎯 Goal: Understand how to interact with the web andextract data from HTML.


import requests
from bs4 import BeautifulSoup


def fetch_headlines(url="https://news.ycombinator.com"):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines
    headlines = []
    for item in soup.select(".titleline a"):
        headlines.append(item.get_text())

    # Display headlines
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline}")


if __name__ == "__main__":
    fetch_headlines()
