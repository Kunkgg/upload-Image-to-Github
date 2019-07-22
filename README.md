# upload-Image-to-Github

A simple script for uploading images to github. It is used for generate link of image quickly in markdown.

## Requirement

- Linux
- xclip
- shutter or other screenshot tool supports save file and save filename to clipboard automatically
- python3

## Usage

Create a github repository for storing images.

Set your github username, repository name and the local directory of images in script.

```sh
usage: gitimages.py [-h] [--source SOURCE] [--update] [--out]

gitImages

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE, -s SOURCE
                        Specify path of image
                        If not specify, it is the latest screenshot(path in clipboard)
  --update, -u          Update all of images in IMAGES_DIR to github
  --out, -o             Whether or not copying the download link of image to clipboard

```
