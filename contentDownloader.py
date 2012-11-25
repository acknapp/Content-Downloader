import urllib2
import BeautifulSoup
import sys
import urlparse

SITE = sys.argv[1]
FILE_TYPES = ["pdf", "doc", "cvs", "jpeg", "jpg", "avi", "mpeg", "rm", "mpg",
              "mp4", "wmv", "rm", "ram", "mov", "mp3"]


def check_file_type(link, extension):
    '''Checks for known file types'''
    return extension in FILE_TYPES


def download_content(site):
    '''Checks each link on a site to see if it is a known filetype'''
    try:
        oSite = urllib2.urlopen(site).read()
        soup = BeautifulSoup.BeautifulSoup(oSite)
        n = 1
        for page in soup.findAll("a"):
            lnk = page['href'].encode('latin-1')
            lnk2 = urlparse.urljoin(site, lnk)
            temp = lnk2.rsplit('.', 1)
            if check_file_type(lnk2, temp[1]):
                print "Downloading file" + str(n)
                download = urllib2.urlopen(lnk2).read()
                file = open('file' + str(n) + "." + temp[1], 'w')
                file.write(download)
                n += 1
    except:
        print site + ": could not be downloaded"


download_content(site)
