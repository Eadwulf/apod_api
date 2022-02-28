import os, requests
from datetime import datetime



def download_image(image_url, full_filepath=None):

    try:
        r = requests.get(image_url).content
        try:
            r = str(r, 'utf-8')
        except UnicodeDecodeError:
            print('Downloading image...') # Debuggin message
            with open(full_filepath, "wb+") as f:
                f.write(r)
            if os.path.isfile(full_filepath):
                print('Image successfully downloded!')
                return True
    except:
        # TODO: Find the error and print it.
        print('An error was encountered during execution')
        return False # Image not downloded!


if __name__ == '__main__':
    # For debbuging porpuses
    image_url = 'https://apod.nasa.gov/apod/image/2112/IridescenzaLunaPleiadi1024.jpg'
    full_filepath = f"{os.path.abspath('.')}/" + '2021-12-04.jpg'
    print(full_filepath)
    download_image(image_url, full_filepath)
