import requests
import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Download fotos by url list'
    )
    parser.add_argument(
        'url_list',
        nargs='+',
        type=str,
        help='Image_url_list'
    )
    parser.add_argument(
        '-n', '--filename',
        type=str,
        default='image',
        help='Basename to files with download images'
    )    
    return parser.parse_args()


def save_image_as_file_in_folder(image, folder_name='images', image_filename='image.jpeg'):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name, image_filename)
    with open(filename, 'wb') as file:
        file.write(image)	


def get_file_extention(url):
	parts = url.split('.')
	if len(parts)>0 and parts[-1] in ('jpg', 'jpeg', 'tif', 'pdf', 'png', 'bmp'):
	    return parts[-1]
	else:
	    return 'jpeg'


def download_image(image_url, image_filename):
    response = requests.get(image_url)
    if not response.ok:
        return('Request error: {0}'.format(response.text))
    save_image_as_file_in_folder(response.content, 
        	image_filename=image_filename)
    return('Image {0} saved as ../images/{1}'.format(image_url, image_filename))

    
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
    args = parse_arguments()
    download_images_by_urls(args.url_list, args.filename)


if __name__ == '__main__':
	main()