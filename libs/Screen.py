from pprint import pprint

class Text_style:
    BLACK = '\033[30m'
    WHITE = '\033[37m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    END_STYLE = '\033[0m'



class Screen(object):
    
    @staticmethod
    def render_line(content, separator = '', padding_left = 4):
        line = ''.ljust(padding_left)
        for i in range(len(content)):
            text = str(content[i][0]) if len(content[i]) > 0 else ''
            align = content[i][1] if len(content[i]) > 1 else None
            style = content[i][2] if len(content[i]) > 2 else None
            line = line + Screen._forge_cell(text, align, style)
            if not i == len(content)-1:
                line = line + separator
        print(line)

    @staticmethod
    def _forge_cell(text, align, style):
        cell = text
        if not align is None:
            cell = align.format(cell)
        if not style is None:
            cell = style + cell + Text_style.END_STYLE
        return cell

    @staticmethod
    def prompt():
        return input(Text_style.YELLOW + "$" + Text_style.WHITE + ": " + Text_style.END_STYLE)
        


class Table(object):

    PADDING = 8
    SEPARATOR = '   '
    HEADER_STYLE = Text_style.BOLD


    #columns_format = ["{:<20}",...]
    def __init__(self, columns_format):
        self.rows = []
        self.n_columns = len(columns_format)
        self.columns_format = columns_format

    # header = ['title1', ...]
    def add_header(self, header):
        row = []
        for column in header:
            row.append(
                [ column, self.HEADER_STYLE ]
                )
        self.add_row(row)


    # row = [ ["value"],... ] or [ ["value", Text_style] ]
    def add_row(self, row):
        self.rows.append(row)

    def add_empty_row(self):
        row = [''] * self.n_columns
        self.rows.append([row])
            

    def render(self):
        for row in self.rows:
            formated_row = []
            for i in range(len(row)):
                cell = [ row[i][0], self.columns_format[i] ]
                if len(row[i]) == 2:
                    cell.append(row[i][1])
                formated_row.append(cell)
            Screen.render_line(formated_row, separator = self.SEPARATOR, padding_left = self.PADDING)
