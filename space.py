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


def fetch_spacex_foto_latest_launch():
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(spacex_url)
    if not response.ok:
    	exit('Request error: {0}'.format(response.text))
    response_json = response.json()
    image_urls = response_json["links"]["flickr_images"]	
    return image_urls


def fetch_hubble_fotos(collection='news'):
    hubble_url = 'http://hubblesite.org/api/v3/image/3811'
    response = requests.get(hubble_url)
    response_json = response.json()
    image_files_list = response_json['image_files']
    return image_urls


def get_file_extention(url):
	parts = url.split('.')
	return parts[-1]


def download_images_by_urls(image_urls, image_file_name='space'):
    for image_index, image_url in enumerate(image_urls, 1):
        ext = get_file_extention(image_url)
        image_filename = '{name}{number}.{extention}'.format(
        	name=image_file_name, 
        	number=image_index,
        	extention=ext
        )
        print(download_image(image_url, image_filename))

def main():
    download_images_by_urls(fetch_spacex_foto_latest_launch(), 'SpaceX')


if __name__ == '__main__':
	main()