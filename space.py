import requests
import os


def save_image_as_file_in_folder(image, folder_name='images', image_filename='image.jpeg'):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name, image_filename)
    with open(filename, 'wb') as file:
        file.write(image)	


def download_image(image_url, image_filename):
    response = requests.get(image_url)
    if not response.ok:
        return('Request error: {0}'.format(response.text))
    save_image_as_file_in_folder(response.content, image_filename=image_filename)
    return('Image saved as ../images/{0}'.format(image_filename))


def main():
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(spacex_url)
    if not response.ok:
    	exit('Request error: {0}'.format(response.text))
    response_json = response.json()
    image_urls = response_json["links"]["flickr_images"]
    for image_index, image_url in enumerate(image_urls, 1):
        image_filename = 'space{number}.jpeg'.format(number=image_index)
        print(download_image(image_url, image_filename))


if __name__ == '__main__':
	main()