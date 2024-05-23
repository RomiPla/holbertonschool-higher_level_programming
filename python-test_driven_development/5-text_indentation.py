#!/usr/bin/python3
"""
    fdhkufhfkfhkfjdv
"""


def text_indentation(text):
    """
       ndsjkdnbvjsd
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tx1 = text.replace('.', '.\n\n').replace('?', '?\n\n')\
        .replace(':', ':\n\n')
    tx = tx1.strip(" ")
    print("{:s}".format(tx))
