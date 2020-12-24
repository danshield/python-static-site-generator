import typer
from ssg.site import Site
import ssg.parsers

def main(source='Content', dest='dist'):
    config = {"source": source, "dest": dest, "parsers": [ssg.parsers.ResourceParser(),
                                                          ssg.parsers.MarkdownParser(),
                                                          ssg.parsers.ReStructuredTextParser()]}
    site = Site(**config).build()



typer.run(main)