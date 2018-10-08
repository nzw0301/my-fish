import argparse
import re
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

parser = argparse.ArgumentParser(description='Extract used BibTex entries in LaTeX file and output them as new bib file')
parser.add_argument('-l',
                    default='main.tex',
                    help='the path to target LaTeX file')
parser.add_argument('-b',
                    default='/Users/nzw/gdrive/papers/library.bib',
                    help='the path to the global BibTeX file including unused BibTeX entries')
parser.add_argument('-o',
                    default='reference.bib',
                    help='the path to output BibTeX file')
args = parser.parse_args()

prog = re.compile(r'\\cite(t|p)*(\[.+?\])*{(.+?)}')
citation_keys = set()
with open(args.l) as f:
    for l in f:
        cites = re.findall(prog, l)
        for cite in cites:
            for entry in cite[2].split(','):
                citation_keys.add(entry.strip())

with open(args.b) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

entries = []

delete_field_names = [
    'abstract', 'keywords', 'url', 'file', 'isbn',
    'doi', 'pmid', 'issn', 'arxivid', 'month'
]

delete_field_names_for_no_arxiv = [
    'eprint', 'prinaryclass', 'archiveprefix'
]

for bib_entry in bib_database.entries:
    if bib_entry['ID'] in citation_keys:
        for field_name in delete_field_names:
            if field_name in bib_entry:
                del bib_entry[field_name]

        if bib_entry.get('journal', '').lower() != 'arxiv':
            for field_name in delete_field_names_for_no_arxiv:
                if field_name in bib_entry:
                    del bib_entry[field_name]

        entries.append(bib_entry)

output_db = BibDatabase()
output_db.entries = entries

writer = BibTexWriter()
writer.indent = ' ' * 4
with open(args.o, 'w') as bibfile:
    bibfile.write(writer.write(output_db))
