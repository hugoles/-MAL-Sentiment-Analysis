#import requeriments

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = 'myanimelist.net/reviews.php?t=anime&filter_check=&filter_hide=&preliminary=on&spoiler=off&p=1'
