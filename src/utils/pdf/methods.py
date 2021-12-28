
from fpdf import FPDF


class PDF(FPDF):

    def set_border_lines(self):
        self.set_line_width(0.0)
        self.line(5.0,5.0,205.0,5.0) # top one
        self.line(5.0,292.0,205.0,292.0) # bottom one
        self.line(5.0,5.0,5.0,292.0) # left one
        self.line(205.0,5.0,205.0,292.0) # right one

    def set_title(self, the_title : str):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt=the_title, border=0)


def create_daily_pdf():
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_border_lines()
    pdf.set_title('Daily')
    pdf.set_author('Silly CLI')
    pdf.output('daily.pdf', 'F')
