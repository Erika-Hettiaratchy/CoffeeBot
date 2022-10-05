import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.allrecipes.com/recipes/134/drinks/coffee/")
soup =  BeautifulSoup(res.text, 'html.parser')
titles = (soup.select('.card__title'))
print(soup.select('a'))


"""<span data-ingredient-name="true">ice</span>"""