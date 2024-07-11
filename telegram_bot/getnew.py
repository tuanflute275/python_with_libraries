import requests
from bs4 import BeautifulSoup

r = requests.get("https://baomoi.com/tag/LITE.epi")
soup = BeautifulSoup(r.text, 'html.parser')
mydiv = soup.find_all('div', {'class':'group/card bm-card relative max-w-full flex w-full [&:not(:first-child)]:mt-[15px] [&:not(:first-child)]:pt-[11px] [&:not(:first-child)]:border-t [&:not(:first-child)]:border-solid [&:not(:first-child)]:border-[#e9ecef]'})
for item in mydiv:
    print(item.div.div.a.href)