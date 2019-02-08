import download_images
import requests
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Fetch image url list by Hubble API from the collection'
    )
    parser.add_argument(
        '-c', '--collection',
        default='news',
        type=str,
        help='collection name in Hubble API'
    )
    parser.add_argument(
        '-n', '--count',
        type=int,
        default=2,
        help='count of photos'
    )  
    parser.add_argument(
        '-p', '--page_number',
        type=int,
        default=1,
        help='page number'
    ) 
    return parser.parse_args()


def fetch_hubble_photo_by_id(hubble_url_template, image_id):
    hubble_api_method = 'image/{id}'.format(id=image_id)
    hubble_image_url = hubble_url_template.format(method=hubble_api_method)
    response = requests.get(hubble_image_url)
    if not response.ok:
        return None
    response_json = response.json()
    image_filename = response_json['image_files'][-1]["file_url"]
    return image_filename


def fetch_hubble_photos_from_collection(
    collection='news',
    hubble_url_template='http://hubblesite.org/api/v3/{method}',
    image_count=2,
    page=1
):
    hubble_api_method = 'images/{collection}'.format(collection=collection)
    hubble_url = hubble_url_template.format(method=hubble_api_method)
    params = {'page': page}
    response = requests.get(hubble_url, params=params)
    if not response.ok:
        exit('Request error: {0}'.format(response.status_code))
    response_json = response.json()
    image_id_list = [image_info["id"] for image_info in response_json]
    image_urls = [
        fetch_hubble_photo_by_id(hubble_url_template, image_id_list[index])
        for index in range(image_count)
    ]
    return image_urls


def main():
    args = parse_arguments()
    image_urls = fetch_hubble_photos_from_collection(collection=args.collection, 
        image_count=args.count, page=args.page_number)
    print(download_images.download_images_by_urls(image_urls, 'Hubble'))


if __name__ == '__main__':
    main()



