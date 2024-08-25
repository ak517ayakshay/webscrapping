from bs4 import BeautifulSoup
import requests
import os

url = "https://www.tataaig.com/health-insurance/cancer-insurance"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    divs = soup.findAll('div', attrs={'class': ['contentClass1']})

    # Create the new BeautifulSoup object with Bootstrap and custom styling
    new_soup = BeautifulSoup('''
    <html>
        <head>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Poppins', sans-serif;
                    background-color: #f8f9fa;
                    margin: 0;
                    padding: 0;
                }
                .header {
                    background-color: #007bff;
                    color: #fff;
                    text-align: center;
                    padding: 20px;
                    border-radius: 8px;
                    margin-bottom: 30px;
                }
                .contentClass1 {
                    background-color: #fff;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    margin-bottom: 20px;
                }
                h2 {
                    font-size: 24px;
                    color: #007bff;
                    margin-bottom: 20px;
                }
                .container {
                    margin-top: 30px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Steps to Claim Cancer Insurance</h1>
                </div>
                <div class="contentArea">
                </div>
            </div>
        </body>
    </html>
    ''', 'html.parser')

    target_text = "The following **Steps need to be followed while requesting an insurance claim"
    content_found = False

    for div in divs:
        if target_text in div.get_text():
            content_found = True
        
        if content_found:
           
            div['class'].append('contentClass1')
            new_soup.find('div', class_='contentArea').append(div)

    if content_found:
        beautified_html = new_soup.prettify()
        folder_path = os.path.join("templates", "cancer.html")

        with open(folder_path, 'w', encoding='utf-8') as file:
            file.write(beautified_html)

        print(f"File saved successfully at {folder_path}")
    else:
        print("Target text not found.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
