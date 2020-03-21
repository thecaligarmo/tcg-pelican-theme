#!/usr/bin/env python

import hashlib 
import os
import inspect
import re
import datetime


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# Make an archive
def backup_file(filename,contents,path):
    today = datetime.date.today()
    tod = today.strftime("%Y.%m.%d")
    put_file_contents(os.path.join(path,"archive/"+filename+"."+tod+".bak"),contents)

def get_file_contents(file):
    f = open(file,"r")
    c = ''
    if f.mode == 'r':
        c = f.read()
    f.close()
    return c

def put_file_contents(file,contents,mode="w"):
    f = open(file,mode)
    f.write(contents)
    f.close()



def get_latex_img(latex, orig, latex_head_contents, className, mdfilename, path):
    # setup contents
    latex_contents = latex_head_contents + '\\begin{document}\n'
    latex_contents += latex
    latex_contents += '\\end{document}\n'

    # Create hash for the latex filename
    latexFileName = mdfilename+hashlib.md5(latex_contents).hexdigest()

    if not os.path.exists(os.path.join(path,"../content/images/latex-cache/"+latexFileName+".png")):
        put_file_contents(latexFileName+".tex",latex_contents)

        os.system("pdflatex "+latexFileName)
        trim = ''
        if className != 'block':
            trim = '-trim '
        os.system("convert -density 300 "+latexFileName+".pdf -quality 90 "+trim+latexFileName+".png")
        os.system("mv "+latexFileName+".png "+os.path.join(path,"../content/images/latex-cache/."))
        os.system("rm "+latexFileName+"*")

    if os.path.exists(os.path.join(path,"../content/images/latex-cache/"+latexFileName+".png")):
        # We want to keep old latex in case there is a problem
        newi = "<img class=\"latex " + className + "\" src=\"{filename}/images/latex-cache/" + latexFileName +".png\" />"
        newi += "<!--" + orig + "-->"
        return newi
    return ""


# Setup our contents
latex_head_contents = '\\documentclass[preview,12pt]{standalone}\n'

# Get abs path
fn = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(fn))

# Grab header content
latex_head_contents += get_file_contents(os.path.join(path,"header.conf"))

# Make sure we actually have the cache dir
ensure_dir(os.path.join(path,"../content/images/latex-cache/"))


for root, dirs, files in os.walk(os.path.join(path,"../content")):
    for file in files:
        if file.endswith(".md"):

            mdfilename = file
            mdfilepath = os.path.join(root, file)
            
            # Grab file contents
            contents = get_file_contents(mdfilepath)
            
            
            # Find first div. We should *always* be starting with divs*
            cdiv = re.search("(<div.*)", contents, re.DOTALL)
            
            # Find all latex tags
            if cdiv:
                html = cdiv.group(0)
                matches1 = re.findall(r"(<latex>.*?</latex>)",html, re.DOTALL)
                matches2 = re.findall(r"(\$\$.*?\$\$)",html, re.DOTALL)
                matched = False

                # If we have matches, we're gonna need archives
                if matches1 or matches2:
                    matched = True
                    backup_file(mdfilename,contents, path)
            
                # For every latex tag do the following
                for i in matches1:
                    # Grab the actual latex
                    latex = '\['+i[7:-8]+'\]'
                    img = get_latex_img(latex, i, latex_head_contents, "block", mdfilename, path)
                    if img:
                        # replace contents
                        contents = re.sub(re.escape(i),img,contents, 0, re.MULTILINE)
                    else:
                        print "ERROR"

                # For every latex tag do the following
                for i in matches2:
                    # Grab the actual latex
                    latex = '$'+i[2:-2]+'$'
                    img = get_latex_img(latex, i, latex_head_contents, "inline", mdfilename, path)
                    if img:
                        # replace contents
                        contents = re.sub(re.escape(i),img,contents, 0, re.MULTILINE)
                    else:
                        print "ERROR"

            
                # reopen the file and rewrite it with the new contents.
                if matched:
                    put_file_contents(mdfilepath,contents)




