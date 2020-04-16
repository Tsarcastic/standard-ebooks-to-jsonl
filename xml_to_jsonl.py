"""To convert ebooks from xml to jsonl."""

import xml.etree.ElementTree as ET
import jsonlines


def parse_xml(xmlfile):
    """To parse the XML file."""
    # create element tree object
    root = ET.parse(xmlfile).getroot()
    return root


def write_dict(parsed_file):
    """To transfer the information to a dictionary."""
    # let's write a dictionary
    working_dict = {}
    for entry in parsed_file:
        for next_level in entry:
            print(next_level.tag)


write_dict(parse_xml('ebooks.xml'))
