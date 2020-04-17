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
    ebooks = []
    for entry in parsed_file:
        if entry.tag == 'entry':
            book = {}
            for entry_child in entry:
                if entry_child.tag in book:
                    book[entry_child.tag].append(entry_child.text)
                else:
                    book[entry_child.tag] = [entry_child.text]
            ebooks.append(book)
    return ebooks

print(write_dict(parse_xml('alt_ebooks.xml')))

write_dict(parse_xml('alt_ebooks.xml'))
