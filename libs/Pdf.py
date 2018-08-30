import pdfkit
import os
from jinja2 import Environment, FileSystemLoader, PackageLoader
from pprint import pprint

class Pdf(object):

    def __init__(self, tpl, filename):
        self.tpl = tpl
        self.filename = filename + '.pdf'
        self.dir = os.path.dirname(os.path.abspath(__file__))

    def create(self, values):
        print("Create " + self.dir)

        env = Environment(
            loader=PackageLoader('templates', '.')
        )

        template = env.get_template('invoice.html')
        rendered = template.render(values)

        pdfkit.from_string(rendered, self.filename)
