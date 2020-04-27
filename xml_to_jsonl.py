"""To convert ebooks from xml to jsonl."""

import xml.etree.ElementTree as ET
import jsonlines


def parse_xml(xmlfile):
    """To parse the XML file."""
    # create element tree object
    root = ET.parse(xmlfile).getroot()
    return root


def convert_ebooks(parsed_file):
    """To transfer the information to a dictionary."""
    # Iterate through the primary element list, ignoring non-book items.
    for entry in parsed_file:

        if entry.tag != 'entry':
            pass

        else:
            book = {}
            source = []
            categories = []
            links = []
            prelink = "https://standardebooks.org"
            
            for entry_child in entry:

                # IF for author element.
                if entry_child.tag == 'author':
                    for author_child in entry_child:
                        if author_child.tag == 'name':
                            book['author'] = str(author_child.text)
                        if author_child.tag == 'uri':
                            book['uri'] = str(author_child.text)

                # Processes 'source' tags as a list instead of a string.
                elif entry_child.tag == 'source':
                    source.append(entry_child.text)

                # Converts XML elements into strings and appends them to list of content
                elif entry_child.tag == 'content':
                    content_string = ''
                    for content_child in entry_child:
                        content_string += ET.tostring(content_child).decode('utf-8')
                        book['content'] = content_string

                # Pulls category terms from the tags and appends them to list of categories
                elif entry_child.tag == 'category':
                    categories.append(entry_child.get('term'))

                # Special rules for links
                elif entry_child.tag == 'link':
                    links.append(prelink + entry_child.get('href'))
                
                elif entry_child.tag == 'publisher' or entry_child.tag == 'rights':
                    pass

                else:
                    book[entry_child.tag] = entry_child.text

            book['source'] = source
            book['categories'] = categories
            book['links'] = links
            yield book


with jsonlines.open('converted_books.jsonl', mode='w') as writer:
    for item in convert_ebooks(parse_xml('ebooks.xml')):
        writer.write(item)
