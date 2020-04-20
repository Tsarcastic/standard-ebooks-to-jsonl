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

                # IF for author element. Currently returns correct but writes "\n\t\t\t"
                if entry_child.tag == 'author':
                    author = {}
                    for author_child in entry_child:
                        author[author_child.tag] = author_child.text


                # IFs to handle tags as a list instead of strings.
                if entry_child.tag == 'source':
                    source.append(entry_child.text)

                # Converts the XML elements into strings and appends them as content
                if entry_child.tag == 'content':
                    for content_child in entry_child:
                        content.append(ET.tostring(content_child).decode('utf-8'))

                # to-do tag == 'category' needs to be adjusted for containing content in tags
                # to-do tag == 'link' needs to be adjusted for containing content in tags


                else:
                    book[entry_child.tag] = entry_child.text
            
            book['source'] = source
            book['content'] = content
            ebooks.append(book)
    return ebooks

with jsonlines.open('test_ebook.jsonl', mode='w') as writer:
    writer.write(write_dict(parse_xml('one_book.xml')))
#write_dict(parse_xml('alt_ebooks.xml'))