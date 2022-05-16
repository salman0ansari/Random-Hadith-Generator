import json
import requests
from bs4 import BeautifulSoup

# TODO 
# - scrape number of hadiths in a book

def write_json(new_data, filename='muslim.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["hadith"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

for i in range(1, 3034):
    obj = {}
    # hadith to scrape
    hname = "muslim" # bukhari, muslim, nasai, abudawud, tirmidhi, ibnmajah
    url = requests.get(f'https://sunnah.com/{hname}:{i}').text
    # source = url.text
    soup = BeautifulSoup(url, 'lxml')

    for hadith in soup.find_all('div', class_='mainContainer'):

        # Book Name
        try: bookName = hadith.find('div', class_='book_page_english_name').text
        except: bookName = 'null'

        # Chapter Name
        try: chapterName = hadith.find('div', class_='englishchapter').text
        except: chapterName = 'null'
        
        # Narrated By
        try: by = hadith.find("div", class_='hadith_narrated').text
        except: by = "null"
        
        # Hadith text
        text = hadith.find("div", class_='text_details').text 
        
        # Hadith Referance
        try: no = hadith.find("div", class_='hadith_reference_sticky').text
        except: no = "null"
        
        obj["id"] = i
        obj["header"] = by
        obj["hadith_english"] = text
        obj["book"] = "Sahih Muslim"
        obj["refno"] = no
        obj["bookName"] = bookName
        obj["chapterName"] = chapterName

    write_json(obj)
    print(i)