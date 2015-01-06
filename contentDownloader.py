#!/usr/bin/python
import urllib2
import BeautifulSoup
import urlparse
import argparse

FILE_TYPES = ["pdf", "doc", "cvs", "jpeg", "jpg", "avi", "mpeg", "rm", "mpg",
              "mp4", "wmv", "rm", "ram", "mov", "mp3"]


def main():
    """main"""
    parser = argparse.ArgumentParser(description="Downloads content off a website")
    parser.add_argument("url", help="The base url to begin downloading")
    parser.add_argument("-f", "--filetypes", help="A file containing a list of file types you would like to download")
    parser.add_argument("-d", "--depth", help="the distance from the base url that you would like to link hop")
    parser.add_argument("-s", "--save", help="directory to save content, default is the current folder")

    args = parser.parse_args()

    if args.filetypes:
        FILE_TYPES = get_types(args.filetypes)

    download_content(args.url)


def get_types(f):
    """Get a list from a file
    :param f
    """
    ftype = []
    with open(f):
        for line in f.readlines():
            ftype.append(line)
    return ftype


def check_file_type(lnk2, extension):
    """Checks for known file types
    :param extension:
    """
    return extension in FILE_TYPES


def download_content(site):
    """Checks each link on a site to see if it is a known filetype
    :param site:
    """
    #TODO: Add recursion
    # try:
    oSite = urllib2.urlopen(site).read()
    soup = BeautifulSoup.BeautifulSoup(oSite)
    n = 1
    for page in soup.findAll("a"):
        lnk = page['href'].encode('latin-1')
        print "lnk: " + lnk #DEBUG
        lnk2 = urlparse.urljoin(site, lnk)
        temp = lnk2.rsplit('.', 1)
        print "lnk2: " + lnk2 #DEBUG
        print "temp: " + temp[1]
        if check_file_type(lnk2, temp[1]):
            print "completes if statement" #DEBUG
            save_content(lnk2, temp[1], n)
            n += 1
    # except:
    #     print site + ": could not be downloaded"


def save_content(url, ext, fname):
    """Saves the content of a url
    :param url
    :param ext
    :param file_num
    """
    #TODO: Add save directory
    #TODO: Make filename more intelligent
    print "Downloading file" + str(file_num)
    download = urllib2.urlopen(url).read()
    file = open('file' + str(file_num) + "." + ext, 'w')
    file.write(download)


if __name__ == "__main__":
    main()
