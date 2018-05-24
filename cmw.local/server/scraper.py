import urllib2

from bs4 import BeautifulSoup
from collections import defaultdict

# debug
from time import sleep

CSV_FILE_PATH = "bands.csv"
HEADER = "id,band,genres\n"
EVERY_NOISE = "http://everynoise.com/engenremap.html"

band_map = defaultdict(set)
main_page = urllib2.urlopen(EVERY_NOISE)

soup = BeautifulSoup(main_page, 'html.parser')
item_number = 1

while True:
    # the div id to go for next
    id_to_try = "item{}".format(item_number)

    # get that div!
    div = soup.find("div", {"id": id_to_try})

    # if it didn't find anything lets assume we are at the end
    if div is None or item_number == 1000:
        print("Proccessed {} genres and {} bands.".format(item_number, len(band_map.keys())))

        # write to CSV
        print("Writing to {}".format(CSV_FILE_PATH))
        with open(CSV_FILE_PATH, "wb+") as csv_file:
            # I always forget this too
            csv_file.write(HEADER)

            for i, band in enumerate(band_map.keys()):
                genres = ",".join(list(band_map[band]))
                # here we use " as the special delimiter for lists
                # hope my catch all unicode encoder strip works
                csv_file.write("{},{},\"{}\"\n".format(i + 1, band.encode('utf-8').strip(), genres.encode('utf-8').strip()))

        break

    # remove the last character since its a weird non-ascii chevron
    genre = div.getText()[:-2]

    genre_link_suffix = genre.replace(" ", "").replace("-", "").replace("&", "").replace(":", "").replace("'", "")
    genre_link = "{}-{}.html".format(EVERY_NOISE.replace(".html", ""), genre_link_suffix)

    genre_page = urllib2.urlopen(genre_link)

    genre_soup = BeautifulSoup(genre_page, 'html.parser')
    genre_item_number = 1

    while True:
        # the div id to go for next
        id_to_try = "item{}".format(genre_item_number)

        # get that div!
        band_div = genre_soup.find("div", {"id": id_to_try})

        # if it didn't find anything lets assume we are at the end
        if band_div is None:
            # end of the list
            break

        # remove the last character since its a weird non-ascii chevron
        band = band_div.getText()[:-2]

        # write to dictionary
        band_map[band].add(genre)

        # I always forget this part
        genre_item_number += 1

    # # I always forget this part
    item_number += 1
    if (item_number) % 100 == 0:
        print("Processsed {} genres".format(item_number))
