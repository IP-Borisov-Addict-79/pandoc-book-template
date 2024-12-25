#!/usr/bin/env python3

'''
This script retrieves TTF files for the Liberation Serif fontset hosted on GitHub:
  - fetch JSON with URL of the binary release archive provided by GitHub developer API;
  - extract URL from JSON;
  - download the archive;
  - unpack the archive;
  - move Serif style TTFs in current directory.

Some details here:
    https://geraldonit.com/2019/01/15/how-to-download-the-latest-github-repo-release-via-command-line/
'''

import os
import requests
from urllib.parse import urlparse
import tarfile
import shutil
import glob

TTFS = {
    'LiberationSerif-BoldItalic.ttf',
    'LiberationSerif-Italic.ttf',
    'LiberationSerif-Bold.ttf',
    'LiberationSerif-Regular.ttf'
}

def get_json(o, r):
    '''
    Fetch JSON via GitHub Developer API.

    Parameters
    ----------
    `o` : organization string (`username` in `github.com/username`)
    `r` : repository string (`repo` in `github.com/username/repo/`)

    Returns
    -------
    `dict()`
    '''
    api_prefix = f'https://api.github.com/repos/{o}/{r}/releases/latest'
    return requests.get(api_prefix).json()

def get_release_url(j, tarball_prefix):
    '''
    Extract URL of the binary release archive from JSON

    Parameters
    ----------
    `j` : JSON converted to `dict()`
    `tarball_prefix` : archive name stripped of version tag and `.tar.gz`
        suffix

    Returns
    -------
    `(archive_name, url)`
    `archive_name` : full archive filename complete with version tag and
        `.tar.gz` suffix
    `url` : URL of the archive file

    Exceptions
    ----------
    `ValueError` : if URL cannot be extracted from retrieved JSON or
        extracted URL is invalid; these may happen due to sudden API change
    '''

    # error messages
    msg_null = 'cannot parse the github releases json - API change?'
    msg_invalid = 'extracted url is invalid: <<URL>>: API change?'

    # extract release tag and generate full archive name
    tag = j['tag_name']
    tarball = f'{tarball_prefix}-{tag}.tar.gz'

    # try to extract the URL
    body = j['body'].split()
    for s in body:
        if tarball in s:
            url = s.replace('(', ' ').replace(')', '').split()[1]
            break
        pass

    # failed to extract the URL
    if 'url' not in locals():
        raise ValueError(msg_null)

    # check if extracted URL is actually an URL
    p = urlparse(url)
    if not all([p.scheme, p.netloc]):
        raise ValueError(msg_invalid.replace('<<URL>>', url))
    return tarball, url

def download_binary_release(url, tgz):
    '''Download filestream from `url`, save it into binary `tgz`.'''
    with open(tgz, 'wb') as f:
        r = requests.get(url)
        f.write(r.content)
        pass
    return

def extract_tarball(arc):
    '''
    Determine the top-level directory in the archive directory structure and
    extract the archive. If there is no top-level directory, then path of
    the curdir (`.`) is returned.

    Arguments
    ---------
    `arc` : path to `tar.gz` archive

    Returns
    -------
    `str()` : name of top-level directory.
    '''

    # determine the top-level directory
    with open(arc, 'rb') as f:
        with tarfile.open(fileobj = f, mode = 'r|gz') as tgz:
            topmem_count = 0    # initialize counter for top-level members
            topdir = '.'        # initialize top-level directory
            for m in tgz.getmembers():    # loop over the archive members
                if '/' in m.name:         # this is not a top-level member,
                    continue              # skip it
                topmem_count += 1         # increase top-level counter
                if topmem_count > 1:      # there is no top-level directory,
                    break                 # stop the count! stop the count!
                if m.isdir():             # this top-level member is a directory,
                    topdir = m.name       # maybe this is the top-level lol
                    pass
                pass
            pass
        pass

    # extract
    with open(arc, 'rb') as f:
        with tarfile.open(fileobj = f, mode = 'r|gz') as tgz:
            # argument for extractall() filter - ignore or block most features
            # specific to UNIX-like filesystems
            # see: https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter
            tgz.extractall(filter = 'data')
            pass
        pass
    return topdir

def install_serif_ttfs(topdir):
    fonts = glob.glob(os.path.join(topdir, '*Serif*.ttf'))
    for font in fonts:
        if not os.path.isfile(os.path.join('.', os.path.basename(font))):
            shutil.move(font, '.')
            pass
        pass
    return

if TTFS.issubset(set(os.listdir())):
    print('ttfs are in place, mothing to do')
    pass
else:
    org  = 'liberationfonts'
    repo = 'liberation-fonts'
    bin_prfx = f'{repo}-ttf'
    json = get_json(org, repo)
    tarball, url = get_release_url(json, bin_prfx)
    download_binary_release(url, tarball)
    topdir = extract_tarball(tarball)
    install_serif_ttfs(topdir)
    pass
