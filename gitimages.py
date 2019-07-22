"""
A simple script for uploading images to github.
It is used for generate link of image quickly in markdown.
"""

import os
import subprocess
import string
import shutil

READ_CLIPBOARD_COMMAND = 'xclip -selection clipboard -out'
WRITE_CLIPBOARD_COMMAND = 'echo {text} | xclip -in -selection clipboard'
UPDATE_GIT_COMMAND = 'git add * && git commit -m "update images" && git push'

IMAGES_DIR = os.path.expanduser('~/Pictures/git-images/')[:-1]
USERNAME = 'Kunkgg'
REPO = 'git-images'
DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/{}/{}/master/'.format(USERNAME, REPO)


def read_clipboard():
    clipboard = subprocess.Popen(
                    READ_CLIPBOARD_COMMAND,
                    shell=True,
                    stdout=subprocess.PIPE).stdout.read()

    return clipboard.decode('utf-8').strip(string.punctuation)

def write_clipboard(text):
    subprocess.Popen(WRITE_CLIPBOARD_COMMAND.format(text=text), shell=True)

def download_link(path):
    return DOWNLOAD_ROOT + os.path.basename(path)

def copy_file(src, dst=IMAGES_DIR):
    if os.path.isfile(src):
        return shutil.copy(src, dst)
    raise FileNotFoundError

def git_update(path):
    os.chdir(path)
    subprocess.Popen(UPDATE_GIT_COMMAND, shell=True)

def cli(source, update, out):

    if not source:
        source = os.path.join('/', read_clipboard())
    
    if not os.path.isfile(source):
        if update:
            git_update(IMAGES_DIR)
            return
        raise FileNotFoundError
    
    if os.path.dirname(source) != IMAGES_DIR:
        copy_file(source)
    
    if out and os.path.isfile(source):
        write_clipboard(download_link(source))

    if update:
        git_update(IMAGES_DIR)


if __name__ == '__main__':
    from argparse import ArgumentParser, RawTextHelpFormatter
    parser = ArgumentParser(description='gitImages',
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument('--source', '-s', action='store', default='', type=str,
                        help='Specify path of image\n'
                        'If not specify, it is the latest screenshot\n')
    parser.add_argument('--update', '-u', action='store_true',
                        help=f'Update all of images in {IMAGES_DIR} to github')
    parser.add_argument('--out', '-o', action='store_true',
                        help='Wether copying the download link of image to clipboard')
    args = parser.parse_args()

    cli(source=args.source, update=args.update, out=args.out)
