import requests
import os
import argparse
import instabot


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Publish photos from the folder to Instagram'
    )
    parser.add_argument(
        'login',
        type=str,
        help='Username in Instagram'
    )
    parser.add_argument(
        'password',
        type=str,
        help='password in Instagram'
    )   
    parser.add_argument(
        'folder',
        type=str,
        help='path to the folder with photos'
    )        
    return parser.parse_args()


def publish_to_instagramm(username, password, folder):
    bot = instabot.Bot()
    bot.login(username=username, password=password)
    if bot.api.last_response.status_code != 200:
        exit(bot.api.last_response)
    file_tree = os.walk(folder)
    image_filenames = []
    for root, dirs, filenames in file_tree:
    	for filename in filenames:
    		image_filenames.append(os.path.join(root, filename))
    for image_filename in image_filenames:
        bot.upload_photo(image_filename, '#space')


def main():
    args = parse_arguments()
    if not os.path.isdir(args.folder):
    	exit("The specified directory '{0}' doesn't exist".format(args.folder))
    publish_to_instagramm(args.login, args.password, args.folder)


if __name__ == '__main__':
	main()