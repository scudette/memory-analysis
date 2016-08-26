#!/usr/bin/python2.7
import os
import re
import stat
import sys
import urllib2

def MakeSymlinks():
    target = os.path.abspath("images")

    for path in os.listdir("."):
        if not re.match(r"\d\d", path):
            continue

        s = os.stat(path)
        dest_link = os.path.join(path, "images")

        if stat.S_ISDIR(s.st_mode) and not os.access(dest_link, os.R_OK):
            print "Creating Symlink %s" % dest_link
            os.symlink(target, dest_link)


def FetchFile(url, filename=None):
    if filename is None:
        filename = "images/" + url.split("/")[-1]

    try:
        os.stat(filename)
    except (OSError, IOError):
        url_handler = urllib2.urlopen(url)
        metadata = url_handler.info()
        file_size = int(metadata.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (filename, file_size)
        block_size = 8192

        with open(filename, "wb") as fd:
            while True:
                data = url_handler.read(block_size)
                if not data:
                    break

                fd.write(data)
                sys.stdout.write(
                    "%10d  [%3.2f%%]\r" % (fd.tell(),
                                           fd.tell() * 100. / file_size))
                sys.stdout.flush()


# Symlinks do not work in windows Alas.
# MakeSymlinks()

base_url = "http://images.rekall-forensic.com/"

# linux images
FetchFile(base_url + "linux/3.16.0-23-generic_amd64.json")
FetchFile(base_url + "linux/3.16.0-23-generic_x86.json")
FetchFile(base_url + "linux/Ubuntu14.10_virtualbox.aff4")

# can't currently find a working link to this
# FetchFile(base_url + "stuxnet.vmem.E01")

# aws
FetchFile(
    base_url + "aws/Windows_Server-2003-R2_SP2-English-32Bit-Base-2015.02.11.aff4")

FetchFile(
    base_url + "aws/Windows_Server-2012-R2_RTM-English-64Bit-Base-2015.02.11.aff4")

FetchFile(base_url + "debianx64.elf.E01")
FetchFile(base_url + "Debian-3.2.0-amd64")
