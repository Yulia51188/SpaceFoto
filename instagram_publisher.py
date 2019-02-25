import requests
import os
import argparse
import instabot
from dotenv import load_dotenv


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Publish photos from the folder to Instagram'
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
        image_filenames = [os.path.join(root, filename) for filename in filenames]
    for image_filename in image_filenames:
        title = os.path.splitext(os.path.basename(image_filename))[0]
        bot.upload_photo(image_filename, '{0}'.format(title))


def main():
    load_dotenv()
    inst_login = os.getenv("INST_LOGIN")
    inst_password = os.getenv("INST_PASSWORD")    
    args = parse_arguments()
    if not os.path.isdir(args.folder):
        exit("The specified directory '{0}' doesn't exist".format(args.folder))
    publish_to_instagramm(inst_login, inst_password, args.folder)


if __name__ == '__main__':
    main()