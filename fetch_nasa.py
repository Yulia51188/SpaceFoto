import download_images
import requests
import argparse
from dotenv import load_dotenv
import os
from datetime import date, timedelta
from itertools import count


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Fetch image url list by NASA API'
    )
    parser.add_argument(
        '-p', '--period',
        type=int,
        default=0,
        help='period for images publication one per day'
    )  
    return parser.parse_args()


def fetch_nasa_image_of_day(key, publication_date, nasa_url):
    payload = {
        'api_key': key,
        'date': publication_date,
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    image = {}
    image["url"] = response.json()["url"]
    image["name"] = response.json()["title"] 
    return image


def fetch_nasa_images_for_period(key, period=0, 
                            nasa_url='https://api.nasa.gov/planetary/apod'):
    current_date = date.today()
    for delta in count(start=0, step=-1):
        day = current_date + timedelta(days=delta)
        yield fetch_nasa_image_of_day(key, day, nasa_url)
        if abs(delta)>=period:
            break
    

def main():
    args = parse_arguments()
    load_dotenv()
    nasa_key = os.getenv("NASA_KEY")
    try:
        image_urls = list(fetch_nasa_images_for_period(
            nasa_key,
            period=args.period,
        ))
        download_images.download_images_by_urls_and_names(image_urls)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()