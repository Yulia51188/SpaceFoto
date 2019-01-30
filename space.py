import requests
import os


def save_file_in_folder(image, folder_name='images', image_name='image.jpeg'):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name, image_name)
    with open(filename, 'wb') as file:
        file.write(image)	


def main():
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    response = requests.get(url)
    save_file_in_folder(response.content, image_name='hubble-bubble.jpeg')


if __name__ == '__main__':
	main()