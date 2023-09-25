from bs4 import BeautifulSoup
import os

for file_name in os.listdir():
    if file_name.endswith(".html"):
        with open(file_name, 'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'html.parser')
            section = soup.find("section", {"class": "display-7"})
            if section:
                section.decompose()
                with open(file_name, 'w') as f:
                    f.write(str(soup))