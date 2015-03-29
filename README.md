# Memory Analysis

Recently the Rekall memory analysis framework implemented a new kind of Web GUI interface. The new interface is modeled after a worksheet - the user simply write a series of parts (Called *CELLs*) inside a single work sheet.  There are a number of cells including, shell commands, markdown, python code and Rekall plugins.

The new medium enables one to write a kind of interactive document, easily embedding code, images, and formatted text inside the document. Not only does the reader have access to the original document, but they can also interact with the worksheet. The Rekall worksheet is completely interactive.

This feature rich interface gave us an idea! If we foster collaboration on a new interactive document we can make it easy for new forensic practitioners to learn and practice memory analysis technique. This can become an awesome teaching tool.

We have given many workshops in the past, and the biggest problem was always time. We always want to cover way more material than there is time for, and so often we must gloss over some parts. With this new tool, users can continue with the exercises in their own time. They could also explore the given images and run their own plugins and add cells (or make notes) at their own leisure.

## The live interactive memory analysis workshop.

This project is therefore a public resource. We wanted to ensure that memory analysis training is available to everyone that wants it. On this web site you will find:

1. The static exported version of all course modules. These modules are produced by the Rekall GUI interface and behave exactly the same way as the regular Rekall GUI, except for any actions which might modify the worksheet (i.e. the worksheets are read only).
2. You can also find here the original source code for all modules, that you can run on your own. If you do this you can modify the worksheet - perhaps add annotations, expand on particular areas or simply explore the given images.

The worksheets are distributed as a git repository. For those who wish to contribute, please just edit the worksheet as you see fit and send us a pull request. We will incorporate useful contributions. We hope this will be a community project and that the overall workshop will grow to cover a lot of material and remain accessible to all.

If you are a teacher and wish to use this resource in your course, please feel free to. This workshop is released under a Creative Commons license (See LICENSE file).

## Setting up an interactive workshop.

Since the workshop discusses a number of images, and interactive session might need to use them it is best to download these images into your repository. We have a script which does this (we dont store large images in the git repo):

    $ git clone https://github.com/scudette/memory-analysis.git
    $ cd source
    $ python ./runme.py

This will download the images into the images directory. It will not download over existing files so it should be safe to run frequently in order to fetch just the newly added images.

Now it is possible to start the web console session:

    $ rekal webconsole --browser source/02-What_is_memory/

To export a worksheet into a static version we can publish:

    $ rekal -v webconsole source/06-Linux_Memory_analysis/ --export www/06-Linux_Memory_analysis/ --export-root-url-path .

This opens the worksheet at `source/06-Linux_Memory_analysis/` and exports it to `www/06-Linux_Memory_analysis/`. Note we specify that the export-root-path (this is the actual directory that will host the root URL of the web site) be the current directory.