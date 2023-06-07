from bs4 import BeautifulSoup
import requests
import sqlite3
import string
import random
import os


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":
    conn = sqlite3.connect("Parser_uakino.db")
    print("Database opened successfully!")

    URL_DOMAIN = r"https://uakino.club"
    URL = r"https://uakino.club/filmy/f/c.year=1921,2023/sort=d.imdb;desc/"
    current_page = 5
    stop_page = 8
    page_url = f"page/{current_page}/"

    while current_page != stop_page:
        page_url = f"page/{current_page}/"
        print("Current page:", current_page)
        page = requests.get(URL + page_url, headers={'User-Agent': 'Custom'})
        print("Status code:", page.status_code)
        soup = BeautifulSoup(page.text, "html.parser")
        films = soup.findAll("div", class_="movie-img")
        for film in films:
            film_release_year = ""
            film_country = ""
            film_genre = ""
            film_director = ""
            film_actors = ""
            film_duration = ""
            film_IMDb_rating = ""

            OUTPUT_SRC = "media\\"
            film_thumb_image_response = requests.get(
                URL_DOMAIN + film.img["src"], headers={'User-Agent': 'Custom'})
            film_thumb_image_output_src = OUTPUT_SRC + id_generator(8) + ".jpg"
            while os.path.isfile(film_thumb_image_output_src):
                film_thumb_image_output_src = OUTPUT_SRC + \
                    id_generator(8) + ".jpg"
            with open(film_thumb_image_output_src, 'wb') as file:
                file.write(film_thumb_image_response.content)
            # film_thumb_image = sqlite3.Binary(
                # film_thumb_image_response.content)

            subpage = requests.get(film.a["href"], headers={
                                   'User-Agent': 'Custom'})
            soup2 = BeautifulSoup(subpage.text, "html.parser")
            film_title = soup2.find("span", class_="solototle").text
            film_description = soup2.find(
                "div", {"itemprop": "description"}).text
            all_info = soup2.findAll("div", class_="fi-item clearfix")
            for info in all_info:
                info_val = info.find("div", class_="fi-desc")
                if info_val != None:
                    info_field = info.find("div", class_="fi-label")
                    if info_field.text == "Рік виходу: ":
                        film_release_year = info_val.text
                    elif info_field.text == "Країна: ":
                        film_country = info_val.text
                    elif info_field.text == "Жанр: ":
                        film_genre = info_val.text
                    elif info_field.text == "Режисер: ":
                        film_director = info_val.text
                    elif info_field.text == "Актори: ":
                        film_actors = info_val.text
                    elif info_field.text == "Тривалість: ":
                        film_duration = info_val.text
                    elif info_field.text == "":  # Rating IMDb
                        film_IMDb_rating = info_val.text
            # insert record into sqlite db
            conn.execute(
                f"INSERT INTO Films (film_title, film_description, film_release_year, film_country, film_genre, film_director,\
             film_actors, film_duration, film_IMDb_rating, film_thumb_image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (film_title, film_description, film_release_year, film_country, film_genre, film_director,
                                                                                                                      film_actors, film_duration, film_IMDb_rating, film_thumb_image_output_src))
        conn.commit()
        current_page += 1
        print("End of parsing of the current page")
    conn.close()
    print("Database closed successfully!")
    print("End!")
