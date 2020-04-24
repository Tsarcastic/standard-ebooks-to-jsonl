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
            categories = []
            links = []

            for entry_child in entry:

                # IF for author element.
                if entry_child.tag == 'author':
                    for author_child in entry_child:
                        print(author_child.tag)
                        if author_child.tag == 'name':
                            book['author'] = str(author_child.text)
                        if author_child.tag == 'uri':
                            book['uri'] = str(author_child.text)

                # Processes 'source' tags as a list instead of a string.
                elif entry_child.tag == 'source':
                    source.append(entry_child.text)

                # Converts XML elements into strings and appends them to list of content
                elif entry_child.tag == 'content':
                    for content_child in entry_child:
                        content.append(ET.tostring(content_child).decode('utf-8'))

                # Pulls category terms from the tags and appends them to list of categories
                elif entry_child.tag == 'category':
                    categories.append(entry_child.get('term'))

                # Special rules for links
                elif entry_child.tag == 'link':
                    link = {}
                    for item in entry_child.attrib.items():
                        link[str(item)] = entry_child.get(item)
                    links.append(link)

                else:
                    book[entry_child.tag] = entry_child.text

            book['source'] = source
            book['content'] = content
            book['categories'] = categories
            book['links'] = links
            ebooks.append(book)
    return ebooks

with jsonlines.open('test.jsonl', mode='w') as writer:
    writer.write(write_dict(parse_xml('one_book.xml')))
