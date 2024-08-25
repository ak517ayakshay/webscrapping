from bs4 import BeautifulSoup
import requests
import os

# Define the URL
url = "https://www.acko.com/health-insurance/senior-citizens/"

# Make a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the required content based on specified class
    quote = soup.findAll('div', attrs={'class': ['ncolumn_rootContainer__8pTf_']})

    # Create a new BeautifulSoup object to hold the modified HTML
    new_soup = BeautifulSoup('<html><body></body></html>', 'html.parser')

    # Append the extracted content to the new BeautifulSoup object
    for i in quote:
        print(i.text)
        # Convert the tag to a string and re-parse it before appending
        new_soup.body.append(BeautifulSoup(str(i), 'html.parser'))

    # Beautify the final HTML
    beautified_html = new_soup.prettify()

    # Create the Templates folder if it doesn't exist
    if not os.path.exists("Templates"):
        os.makedirs("Templates")

    # Define the file path for saving in the Templates folder
    folder_path = os.path.join("Templates", "senior.html")

    # Save the beautified HTML content to the specified file path
    with open(folder_path, 'w', encoding='utf-8') as file:
        file.write(beautified_html)

    print(f"File saved successfully at {folder_path}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
