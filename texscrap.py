#!/usr/bin/env python

import argparse
import os
from jinja2 import Environment, FileSystemLoader
import subprocess 
import tempfile 
import time 
import sys 

__author__ = 'John Joseph Horton'
__description__ = 'Runs pdflatex on a LaTeX file that lacks a header and returns a tightly cropped PDF, and optionally, a PNG file. Can also run on a quoted LaTeX equation'
__copyright__ = 'Copyright (C) 2012  John Joseph Horton'
__license__ = 'GPL v3'
__maintainer__ = 'johnjosephhorton'
__email__ = 'john.joseph.horton@gmail.com'
__status__ = 'Development'
__version__ = '0.1'

def make_pdf(file_name, output_file_name, seq = ['p', 'p']): 
    '''
    Given a filename, creates a PDF using pdflatex. The seq argument allows
    for multiple runs of pdflatex is needed. 
    '''
    for op in seq: 
        print("Doing a %s iteration" % op)         
        if op is 'p':
            pdftex_process = subprocess.Popen(['pdflatex', 
                                               '-interaction=nonstopmode', 
                                               '%s'%file_name], 
                                              shell=False, 
                                              stdout=subprocess.PIPE)
            print("PDFTEX return code is %s" % pdftex_process.returncode)
            if pdftex_process.returncode != 0:
                message = pdftex_process.communicate()[0].decode() 
                txt = message.split("\n")
                for l in txt:
                    if len(l) > 0 and l[0]=='!':
                        print(l)
        os.system("mv %s %s" % (file_name.replace(".tex", ".pdf"), output_file_name)) 
    return None 

def crop_pdf(input_file, output_file):
    '''
    Wrapper for the pdfcrop function---crops the input_file to a tight box
    around the image/text. 
    '''
    try: 
        os.system('pdfcrop %s %s' % (input_file, output_file))
        return True
    except: 
        return False 


def pdf2png(input_file, output_file):
    '''
    Wrapper for ImageMagick convert utility. 
    '''
    try: 
        os.system("convert -density 400 %s %s" % (input_file, output_file))
        return True 
    except: 
        return False

def cleanup(base_file_name): 
    '''
    Cleans up all the LaTeX cruff generated when making the file. 
    '''
    os.remove(base_file_name + "_wrapped.tex")
    os.remove(base_file_name + "_wrapped.aux")
    os.remove(base_file_name + "_wrapped.log")
    os.remove(base_file_name + "_wrapped.out")

def main():
    loader = FileSystemLoader(
            os.path.join(os.path.dirname(
                os.path.abspath(__file__)), 'templates'))
    env = Environment(loader=loader)
    parser = argparse.ArgumentParser(
        description=__description__)
    parser.add_argument("-f", "--file", help="File to render")
    parser.add_argument("-e", "--equation", help="Equation to render")
    parser.add_argument("--png",
                        action="store_true",
                        default=False,
                        help="Creat a companion PNG file.")
    args = parser.parse_args()
    if args.file:
        tex_file_name = args.file
    elif args.equation: 
        tex_file_name = "equation_file" + str(int(time.time())) + ".tex"
        with open(tex_file_name, "w") as f: 
            f.write("$" + args.equation + "$")
            f.close()
    else: 
        tex_file_name = "stdin_file" + str(int(time.time())) + ".tex"
        g = open(tex_file_name, "w")
        for line in sys.stdin.readlines():
            g.write(line)
        g.close()
            
    base_file_name = tex_file_name.replace(".tex", "")
    wrapped_snippet_file_name = base_file_name + "_wrapped.tex"
    pdf_file_name = base_file_name + ".pdf" 
    png_file_name = base_file_name + ".png"
    
    with open(tex_file_name, "r") as f:
        wrapped_snippet = env.get_template("latex_wrapper.tex").render(body = ''.join(f.readlines()))
        f.close()
    with open(wrapped_snippet_file_name, "w") as g:
        g.writelines(wrapped_snippet)
        g.close()
    make_pdf(wrapped_snippet_file_name, pdf_file_name)
    crop_pdf(pdf_file_name, pdf_file_name)
    if args.png: 
        pdf2png(pdf_file_name, png_file_name)
    
    cleanup(base_file_name)         

if __name__ == '__main__':
    main()
