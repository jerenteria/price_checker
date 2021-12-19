from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

## look for $ in browser and store it in prices variable
prices = doc.find_all(text="$")
## finds the parent tag of $ which acutally tells the price of item
parent = prices[0].parent
## use "strong" because thats the tag they use to display price
strong = parent.find("strong")
## prints out strong tag in string which is just the price itself
print(strong.string)