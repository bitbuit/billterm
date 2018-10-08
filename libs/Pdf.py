import pdfkit
import os
from jinja2 import Environment, FileSystemLoader, PackageLoader
from pprint import pprint

class Pdf(object):

    def __init__(self, tpl, filename):
        self.tpl = tpl
        self.filename = filename + '.pdf'
        self.dir = os.path.dirname(os.path.abspath(__file__))

    def _add_util_values(self, values):
        full_values = values
        full_values['PDF_FILENAME'] = self.filename
        full_values['ABS_PATH'] = self.dir + '/../'
        return full_values

    def create(self, values):
        print("Create " + self.dir)

        env = Environment(
            loader=PackageLoader('templates', '.')
        )

        template = env.get_template('invoice.html')
        rendered = template.render(self._add_util_values(values))

        pdfkit.from_string(rendered, 'documents/' + self.filename)
