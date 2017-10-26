#!/usr/bin/python3

import argparse
import sys
from xml.dom import minidom

def print_tabs(str, tab_level, end='\n'):
    for _ in range(tab_level):
        print('\t',end='')

    print(str,end=end)

def print_node(node, tab_level):
    child_level = tab_level
    if(node.nodeType == 1):
        print_tabs('<' + node.nodeName, tab_level)

        for name,value in sorted(node.attributes.items()):
            print_tabs(' ' + name + ' = "' + value + '"', tab_level)

        if(len(node.childNodes) < 1):
            print_tabs('/>', tab_level)
            return
        else:
            print_tabs('>', tab_level)

        child_level = tab_level + 1

    for child in sorted(node.childNodes, key=lambda node: node.nodeName):
        print_node(child,child_level)

    if(node.nodeType == 1):
        print_tabs('</' + node.nodeName + '>', tab_level)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()

    if args.filename:
        xml_file = open(args.filename,'r')
    elif not sys.stdin.isatty():
        xml_file = sys.stdin
    else:
        parser.print_help()
        sys.exit(1)

    xml_doc = minidom.parse(xml_file)
    xml_file.close()

    print_node(xml_doc,0)
