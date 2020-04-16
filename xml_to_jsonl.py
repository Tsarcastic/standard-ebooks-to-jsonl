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
    # Iterate through the parsed file
    for entry in parsed_file:
        if entry.tag == '{http://www.w3.org/2005/Atom}entry':
            # Position set at 29 to correctly grab title
            # Currently will print "title" followed by title
            current_count = 1
            current_entry = entry[current_count]
            print((current_entry.tag)[29:], current_entry.text)


write_dict(parse_xml('ebooks.xml'))
