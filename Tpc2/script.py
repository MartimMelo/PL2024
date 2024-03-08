import sys
import re


def header_converter(match):
    return f"<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>"

def list_converter(match):
    return f"<ol>\n\t{"\n\t".join([i for i in match.group(1).split('\n')])}\n</ol>"


def markdown_to_html_converter(md):
    
    md = re.sub(r'(#+) +(.+)', header_converter, md) # Headers   
    md = re.sub(r'\*\*(.+)\*\*', r'<b>\1</b>', md) # Bold
    md = re.sub(r'\*(.+)\*', r'<i>\1</i>', md) # Italics
    md = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', md, flags=re.MULTILINE) # Numbered lists
    md = re.sub(r'(<li>.+</li>)+', list_converter, md, flags=re.DOTALL | re.MULTILINE) # Numbered lists
    md = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', md) # Image
    md = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', md) # Link

    return md


if __name__ == "__main__":

    with open(sys.argv[1], 'r') as file_read: 
        html_output = markdown_to_html_converter(file_read.read())
    file_read.close()

    with open(sys.argv[2], 'w') as file_write: 
        file_write.write(html_output)
    file_write.close()
