#import requeriments

import requests
import pandas as pd
from colorama import init, Fore
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

import requests
from bs4 import BeautifulSoup
from colorama import Fore

def myanimelist(n_pages):
    for n_page in range(n_pages):
        # Set the URL of the page you want to scrape
        url = f'https://myanimelist.net/reviews.php?t=anime&filter_check=&filter_hide=&preliminary=on&spoiler=off&p={n_page}'

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all review elements on the page
            review_elements = soup.find_all(class_='review-element js-review-element')

            # Iterate through each review element and extract relevant information
            for review in review_elements:
                # Extract the title of the anime from the review element
                anime_title = review.find(class_='title ga-click').text.strip()

                # Extract the numerical rating from the review element
                rating_element = numerical_rating = review.find(class_='rating mt20 mb20 js-hidden')
                numerical_rating = rating_element.find(class_='num').text.strip()

                # Extract the text of the review from the review element
                review_text = review.find(class_='text').text.strip()

                # Print the extracted information
                print(f'Title: {anime_title}')
                print(f'Rating: {numerical_rating}')
                print(f'Review: {Fore.WHITE}{review_text}{Fore.RESET}\n')
        else:
            print(f'Failed to retrieve the page. Status code: {response.status_code}')


if __name__ == '__main__':
    input_number = int(input('Enter the number of pages: '))
    myanimelist(input_number)