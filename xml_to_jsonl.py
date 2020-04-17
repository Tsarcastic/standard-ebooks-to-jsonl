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

    # Iterate through the primary element list, looking for books.
    for entry in parsed_file:
        if entry.tag == 'entry':
            book = {}
            source = []
            content = []

            for entry_child in entry:

                # IF for author element.
                if entry_child.tag == 'author':
                    author = {}
                    for author_child in entry_child:
                        author[author_child.tag] = author_child.text
                    book['author'] = author

                if entry_child.tag == 'source':
                    source.append(entry_child.text)

                if entry_child.tag == 'content':
                    for content_child in entry_child:
                        content.append(content_child.text)


                else:
                    book[entry_child.tag] = entry_child.text
            book['source'] = source
            book['content'] = content
            ebooks.append(book)
    return ebooks

print(write_dict(parse_xml('alt_ebooks.xml')))