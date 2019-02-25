import download_images
import requests
import argparse
from dotenv import load_dotenv
import os


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Fetch image url list by NASA API'
    )
    parser.add_argument(
        '-n', '--count',
        type=int,
        default=2,
        help='count of photos'
    )  
    return parser.parse_args()


def fetch_nasa_image_of_day(
    key,
    nasa_url='https://api.nasa.gov/planetary/apod',
):
    payload = {
        'api_key': key,
        'date': '2019-01-01'
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    image = {}
    image["url"] = response.json()["hdurl"]
    image["name"] = response.json()["title"] 
    return image

def main():
    args = parse_arguments()
    load_dotenv()
    nasa_key = os.getenv("NASA_KEY")
    try:
        image_urls = [(fetch_nasa_image_of_day(nasa_key))]
        print(image_urls)
        download_images.download_images_by_urls_and_names(image_urls)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()