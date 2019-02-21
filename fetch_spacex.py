import download_images
import requests


def fetch_spacex_photo_latest_launch(
    spacex_url='https://api.spacexdata.com/v3/launches/latest'
):
    response = requests.get(spacex_url)
    response.raise_for_status()
    response_json = response.json()
    image_urls = [
        {
            'url':image_url, 
            'name': '{name}_{index}'.format(name=response_json['mission_name'], 
                                            index=index)
        } 
        for index, image_url in enumerate(
            response_json['links']['flickr_images'], 1)
    ]
    return image_urls


def main():
    try:
        image_urls = fetch_spacex_photo_latest_launch()
        download_images.download_images_by_urls_and_names(image_urls)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()
