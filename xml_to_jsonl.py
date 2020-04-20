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

                # IF for author element. Currently returns correct but writes "\n\t\t\t"
                if entry_child.tag == 'author':
                    author = {}
                    for author_child in entry_child:
                        author[author_child.tag] = author_child.text

                # Processes 'source' tags as a list instead of a string.
                if entry_child.tag == 'source':
                    source.append(entry_child.text)

                # Converts the XML elements into strings and appends them to list of content
                if entry_child.tag == 'content':
                    for content_child in entry_child:
                        content.append(ET.tostring(content_child).decode('utf-8'))

                # Pulls the category terms from the tags and appends them to list of categories
                if entry_child.tag == 'category':
                    categories.append(entry_child.get('term'))

                if entry_child.tag == 'link':
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

with jsonlines.open('test_ebook.jsonl', mode='w') as writer:
    writer.write(write_dict(parse_xml('one_book.xml')))
#write_dict(parse_xml('alt_ebooks.xml'))