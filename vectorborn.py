from bs4 import BeautifulSoup
import requests

url = "https://www.acko.com/health-insurance/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    quote=soup.findAll('div',attrs={'class':'sc-bdVaJa sc-bwzfXH sc-iujRgT gtOBw'})
    new_soup = BeautifulSoup('<html><body></body></html>', 'html.parser')
    for i in quote:
        print(i.text)
        new_soup.body.append(i)
    beautified_html = new_soup.prettify()
    with open('vectorborn.html', 'w', encoding='utf-8') as file:
            file.write(beautified_html)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
