import download_images
import requests


def fetch_spacex_photo_latest_launch(
    spacex_url='https://api.spacexdata.com/v3/launches/latest'
):
    response = requests.get(spacex_url)
    if not response.ok:
        exit('Request error: {0}'.format(response.text))
    response_json = response.json()
    image_urls = response_json["links"]["flickr_images"]	
    return image_urls


def main():
    image_urls = fetch_spacex_photo_latest_launch()
    download_images.download_images_by_urls(image_urls, 'SpaceX')


if __name__ == '__main__':
    main()
