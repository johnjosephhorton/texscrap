texscrap
========
`texscrap` is a Python utility from turning snippets of LaTeX--either files (via `--file`) or equations (via `--equation`) into tightly bound stand-alone PDFs (and optionally, PNGs, via `--png` flag). 
The resultant files are written the directory the script is called from. 
If you use the `--equation` option, a file `equation_<unix timestamp>.tex` is written into your directory. 

The primary use case is getting image files for inclusion in a presentation. 
Even if you are using a Beamer class for presentations, it is often useful to include images of tables and equations rather than the actual TeX since the re-sizing options are more flexible. 

The actual LaTeX "wrapper" is in the directory `./templates` and can be easily modified with the pacakges you need. 

Dependencies
------------

In addition to `jinja2`, this script also requires [pdflatex](http://www.tug.org/applications/pdftex/), [ImageMagick](http://www.imagemagick.org/script/index.php) and [pdfcrop](http://www.ctan.org/pkg/pdfcrop).  

To install
----------

    git clone git@github.com:johnjosephhorton/texscrap.git
	cd texscrap 
	sudo python setup.pu install 

Example
-------

To render an equation, we can run: 

    texscrap -e "\int_x^y dx"

which creates the file [equation_file1374688256.pdf](https://dl.dropboxusercontent.com/u/420874/permanent/equation_file1374688256.pdf). 

Documentation
-------------
```
usage: texscrap.py [-h] [-f FILE] [-e EQUATION] [--png]

Runs pdflatex on a LaTeX file that lacks a header and returns a tightly
cropped PDF, and optionally, a PNG file. Can also run on a quoted LaTeX
equation

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to render
  -e EQUATION, --equation EQUATION
                        Equation to render
  --png                 Creat a companion PNG file.
```

=======

