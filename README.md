# SpaceFoto

The project includes 4 modules: 
- `instagram_publisher.py` - it publicates all photos in the specified folder (including subdirectories), uses [Instabot](https://instagrambot.github.io/docs/en/For_developers.html#photos)
- `download_images.py` - it downlods images by url list
- `fetch_hubble.py` - it fetchs images url list from the specified photo collection of Hubble telescope, using [Hubble API](http://hubblesite.org/api/documentation)
- `fetch_spacex.py` - it fetchs images url list from the latest launch photo collection of SpaceX, using [SpaceX API](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1)

# How to install

To publish photos to Instagram you need account username and password. You can get it after registration in [Instagram](http://instagram.com) or use existing one.

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```python
pip install -r requirements.txt
```

# How to launch

- Download photos to the local machine
To download photos from SpaceX the latest launch (all examples are for Linux):
```bash
$ python3 fetch_spacex.py 
Image https://farm5.staticflickr.com/4866/39745612523_14270b4b9d_o.jpg saved as ../images/SpaceX1.jpg
Image https://farm8.staticflickr.com/7833/39745612923_21aa442350_o.jpg saved as ../images/SpaceX2.jpg

```
See terminal output to know paths and image names.

To download photos from Hubble site firstly read help with description of available arguments. All arguments are optional, so you can launch script as:
```bash
$ python3 fetch_hubble.py
Image https://media.stsci.edu/uploads/image_file/image_attachment/31220/STSCI-H-p1909a-f-1355x1017.png saved as ../images/Hubble1.png
Image https://media.stsci.edu/uploads/image_file/image_attachment/31222/STSCI-H-p1909b-f-1355x1017.png saved as ../images/Hubble2.png
```

or input another collection name and/or image count:

```bash
$ python3 fetch_hubble.py --collection stsci_gallery --count 4
Image https://media.stsci.edu/uploads/image_file/image_attachment/30510/STScI-gallery-1529a-2000x960.jpg saved as ../images/Hubble1.jpg
Image https://media.stsci.edu/uploads/image_file/image_attachment/30511/STScI-gallery-1512a-2000x960.jpg saved as ../images/Hubble2.jpg
Image https://media.stsci.edu/uploads/image_file/image_attachment/30516/STScI-gallery-1501c-2000x960.jpg saved as ../images/Hubble3.jpg
Image https://media.stsci.edu/uploads/image_file/image_attachment/30589/STScI-gallery-1427a-2000x960.jpg saved as ../images/Hubble4.jpg
```
- Publish photos to Instagram

```bash
$ python3 instagram_publisher.py Yulia51188 Secretar6a images/
```
The terminal output includes log information from Instabot with result of publishing.

The launch in Windows and MacOs is the same.

# Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
