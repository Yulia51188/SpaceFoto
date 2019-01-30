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
    save_image_as_file_in_folder(response.content, image_filename=image_filename)


def main():
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_image(url, 'hubble.jpeg')


if __name__ == '__main__':
	main()