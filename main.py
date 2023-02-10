import requests
from bs4 import BeautifulSoup
#Code to recieve recipes from the website.
res = requests.get("https://www.allrecipes.com/recipe/235850/starbucks-caramel-frappuccino-copycat-recipe/")
soup = BeautifulSoup(res.text, 'html.parser')
#The specific ingredients we want.
soupspan = soup.select('li.mntl-structured-ingredients__list-item span')


#loop to remove <span>
i = 0
for s in soupspan:
  decoded = (s.decode_contents())
  if i <= 2:
    print(decoded, end = " ")
    i += 1
  if i == 3:
    i = 0
    print(",")
