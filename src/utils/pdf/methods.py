
from fpdf import FPDF
import requests
from ..services import get_multiple_dad_jokes


# Template PDF containing a list of jokes
# For sad days, to cheer up! :D
class JOKES_PDF(FPDF):

    BORDER_LINE_WIDTH = 0.0
    LEFTMOST_POINT    = 5.0
    RIGHTMOST_POINT   = 205.0
    UPPERMOST_POINT   = 5.0
    LOWERMOST_POINT   = 292.0
    TITLE_FONT        = 'Arial'
    TEXT_FONT         = 'Times'
    TEXT_SIZE         = 12
    TITLE             = 'Daily Jokes'
    AUTHOR            = 'Silly CLI - Jokes division'
    LOGO1_PATH        = './static/photos/laugh.png'
    LOGO2_PATH        = './static/photos/smile.jpg'
    TITLE_RGB         = (0, 153, 51)
    TEXT_RGB          = (204, 0, 153)

    def header(self):
        self.image(JOKES_PDF.LOGO1_PATH, 10, 8, 33)
        self.image(JOKES_PDF.LOGO2_PATH, 169, 8, 33)
        self.set_font(JOKES_PDF.TITLE_FONT, 'B', 15)
        self.set_text_color(JOKES_PDF.TITLE_RGB[0], JOKES_PDF.TITLE_RGB[1], JOKES_PDF.TITLE_RGB[2])
        # Move to the right
        self.cell(80)
        self.cell(30, 10, JOKES_PDF.TITLE, 0, 0, 'C')
        # Line break
        self.ln(40)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font(JOKES_PDF.TITLE_FONT, 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def set_border_lines(self):
        self.set_line_width(JOKES_PDF.BORDER_LINE_WIDTH)
        self.line(JOKES_PDF.LEFTMOST_POINT,   JOKES_PDF.UPPERMOST_POINT, JOKES_PDF.RIGHTMOST_POINT, JOKES_PDF.UPPERMOST_POINT)
        self.line(JOKES_PDF.LEFTMOST_POINT,   JOKES_PDF.LOWERMOST_POINT, JOKES_PDF.RIGHTMOST_POINT, JOKES_PDF.LOWERMOST_POINT)
        self.line(JOKES_PDF.LEFTMOST_POINT,   JOKES_PDF.UPPERMOST_POINT, JOKES_PDF.LEFTMOST_POINT,  JOKES_PDF.LOWERMOST_POINT)
        self.line(JOKES_PDF.RIGHTMOST_POINT,  JOKES_PDF.UPPERMOST_POINT, JOKES_PDF.RIGHTMOST_POINT, JOKES_PDF.LOWERMOST_POINT)

    def add_joke(self, txt: str, index: int):
        txt = txt.encode('latin-1', 'replace').decode('latin-1') # Hackish workaround
        txt = str(index) + ') ' + txt
        self.set_text_color(JOKES_PDF.TEXT_RGB[0], JOKES_PDF.TEXT_RGB[1], JOKES_PDF.TEXT_RGB[2])
        self.multi_cell(0, 10, txt, 0, 1)

    def generate():
        pdf = JOKES_PDF(orientation='P', unit='mm', format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_border_lines()
        pdf.set_author(JOKES_PDF.AUTHOR)
        pdf.set_font(JOKES_PDF.TEXT_FONT, '', JOKES_PDF.TEXT_SIZE)
        return pdf


def create_daily_pdf(number_of_jokes: int = 5):
    """
    Generates a PDF file with jokes.

    :param number_of_jokes: How many jokes to be added to the PDF file
    """
    pdf = JOKES_PDF.generate()
    jokes = get_multiple_dad_jokes(number_of_jokes)
    for index, joke in enumerate(jokes):
        pdf.add_joke(joke, index + 1)
    pdf.output('daily.pdf', 'F')
