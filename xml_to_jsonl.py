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
        if entry.tag == 'entry':
            # Currently will print "title" followed by title
            current_count = 1
            print(entry[current_count].tag, entry.[current_count].text


write_dict(parse_xml('alt_ebooks.xml'))
