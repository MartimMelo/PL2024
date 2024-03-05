import sys
import re

def bold_sub(line):
    bold_regex = re.compile(r'\*\*(.*?)\*\*')
    return bold_regex.sub(r'<b>\1</b>', line)

def it_sub(line):
    italic_regex = re.compiler(r'\*(.*?)\*')
    return italic_regex.sub(r'<i>\1</i>', line)

def link_sub(line):
    link_regex = re.compile(r'(\[)(.*?)(\])\((.*?)\)')
    return link_regex.sub(r'<a href="\4">\2</a>', line)

#![imagem dum coelho](http://www.coellho.com)
#<img src="http://www.coellho.com" alt="imagem dum coelho"/>

def img_sub(line):
    img_regex = re.compile(r'(\!\[)(.*?)(\])\((.*?)\)')
    return img_regex.sub(r'<img src="\4" alt="\2"/>')
    
