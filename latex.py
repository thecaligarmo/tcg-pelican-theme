#!/usr/bin/env python

import hashlib
import os
import shutil
import inspect
import re
from PIL import Image


# Must start with ./ and end with /
cache_dir = './content/images/latex-cache/'
latex_content_dir = './latex/'
content_dir = './content/'


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_file_contents(file):
    f = open(file, "r")
    c = ''
    if f.mode == 'r':
        c = f.read()
    f.close()
    return c


def put_file_contents(file, contents, mode="w"):
    ensure_dir(file)
    f = open(file, mode)
    f.write(contents)
    f.close()


def get_latex_img(latex, class_name, mdfilename, path):
    orig = latex

    # Grab header content
    latex_head_contents = '\\documentclass[preview, 12pt]{standalone}\n'
    latex_head_contents += get_file_contents(os.path.join(path, "header.conf"))

    # setup contents
    latex_contents = latex_head_contents + '\\begin{document}\n'
    latex_contents += latex
    latex_contents += '\\end{document}\n'

    # Create hash for the latex filename
    latex_file_name = mdfilename+hashlib.md5(latex_contents).hexdigest()
    img_file_path = os.path.join(path, cache_dir+latex_file_name+".png")
    tmp_path = os.path.join(path, "./tmp/")
    latex_file_path = tmp_path+latex_file_name
    src_file_path = cache_dir.replace('./content', '')

    if not os.path.exists(img_file_path):
        put_file_contents(latex_file_path+'.tex', latex_contents)

        pdf_made = os.system("pdflatex -output-directory " + tmp_path[:-1]
                             + ' '+latex_file_path+'.tex')
        if pdf_made == 0:
            convert_options = ""
            convert_options += "-quality 100 "
            convert_options += "-flatten "
            convert_options += "-resize 20% "
            convert_options += "-trim "
            convert_options += "-transparent white "
            convert_options += "-fuzz 10% "
            os.system("convert -density 1440 " + latex_file_path + ".pdf "
                      + convert_options + latex_file_path+".png")
            os.system("mv " + latex_file_path+".png " + img_file_path)
            os.system("rm " + latex_file_path + "*")

    if os.path.exists(img_file_path):
        # Get height:
        im = Image.open(img_file_path)
        w, h = im.size

        # We want to keep old latex in case there is a problem
        new_i = "<img "
        new_i += "class=\"latex " + class_name + "\" "
        new_i += "src=\"{static}" + src_file_path + latex_file_name + ".png\" "
        new_i += "style=\"height:" + str(h/3) + "px\" />"
        new_i += "<!--" + orig + "-->"
        return new_i
    return ""


# Get abs path
fn = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(fn))

tmp_path = os.path.join(path, "./tmp/")
ensure_dir(tmp_path)
for filename in os.listdir(tmp_path):
    file_path = os.path.join(tmp_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


# Make sure we actually have the cache dir
ensure_dir(os.path.join(path, cache_dir))
ld = os.path.join(path, latex_content_dir)
for root, dirs, files in os.walk(ld):
    for file in files:
        if file.endswith(".md"):

            mdfilename = file
            mdfilepath = os.path.join(root, file)

            # Grab file contents
            contents = get_file_contents(mdfilepath)

            matches1 = re.findall(r"(<latex>.*?</latex>)", contents, re.DOTALL)
            matches2 = re.findall(r"(\$\$.*?\$\$)", contents, re.DOTALL)

            # For every latex tag do the following
            for i in matches1:
                # Grab the actual latex
                class_name = 'block'
                if i[7] == '$':
                    class_name = 'inline'

                img = get_latex_img(i[7:-8], class_name,  mdfilename, path)
                if img:
                    # replace contents
                    contents = re.sub(
                            re.escape(i),
                            img.replace('\\', '\\\\'),
                            contents,
                            0,
                            re.MULTILINE
                        )
                else:
                    print("ERROR")

            # For every latex tag do the following
            for i in matches2:
                # Grab the actual latex
                img = get_latex_img(i[1:-1], 'inline', mdfilename, path)
                if img:
                    # replace contents
                    contents = re.sub(
                            re.escape(i),
                            img.replace('\\', '\\\\'),
                            contents,
                            0,
                            re.MULTILINE
                        )
                else:
                    print("ERROR")

            # reopen the file and rewrite it with the new contents.
            new_root = root.replace(latex_content_dir, content_dir)
            new_mdfilepath = os.path.join(new_root, mdfilename)
            put_file_contents(new_mdfilepath, contents)
