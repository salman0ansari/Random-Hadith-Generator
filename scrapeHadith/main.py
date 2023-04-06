import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm


BOOK_NAME = "Jami` at-Tirmidhi"
TOTAL_HADITH = 3956
SCRAPE_HADITH = "tirmidhi"  # bukhari, muslim, nasai, abudawud, tirmidhi, ibnmajah
FILE_NAME = "tirmidhi.json"


async def fetch_hadith(session, url):
    async with session.get(url) as response:
        return await response.text()


def write_json(new_data, filename=FILE_NAME):
    try:
        with open(filename, "r") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        file_data = {"hadith": []}
    file_data["hadith"].append(new_data)
    with open(filename, "w") as file:
        json.dump(file_data, file, indent=4)


async def process_hadith(i, hname, session, pbar):
    url = f"https://sunnah.com/{hname}:{i}"
    source = await fetch_hadith(session, url)
    soup = BeautifulSoup(source, "lxml")
    hadiths = soup.find_all("div", class_="mainContainer")

    for hadith in hadiths:
        # Book Name
        try:
            bookName = hadith.find("div", class_="book_page_english_name").text
        except:
            bookName = "null"

        # Chapter Name
        try:
            chapterName = hadith.find("div", class_="englishchapter").text
        except:
            chapterName = "null"

        # Narrated By
        try:
            by = hadith.find("div", class_="hadith_narrated").text
        except:
            by = "null"

        # Hadith text
        try:
            text = hadith.find("div", class_="text_details").text
        except:
            text = "null"

        # Hadith Reference
        try:
            no = hadith.find("div", class_="hadith_reference_sticky").text
        except:
            no = "null"

        obj = {
            "id": i,
            "header": by,
            "hadith_english": text,
            "book": BOOK_NAME,
            "refno": no,
            "bookName": bookName,
            "chapterName": chapterName,
        }
        write_json(obj)
    pbar.update(1)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        with tqdm(total=TOTAL_HADITH) as pbar:
            for i in range(1, TOTAL_HADITH):
                task = asyncio.create_task(
                    process_hadith(i, SCRAPE_HADITH, session, pbar)
                )
                tasks.append(task)
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
