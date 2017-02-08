# pylint: disable=W0104, line-too-long, C0325
"""Give the answer of a sudoku puzzle"""
import random
from fpdf import FPDF

def create_empty_playing_field():
    """Create an empty playing field"""
    playing_field = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return playing_field

def fill_square(playing_field, x_coord, y_coord, value):
    """Fill a square with a number"""
    playing_field[y_coord][x_coord] = int(value)

# Still produces some incorrect results
def fill_sudoku(playing_field):
    """Fill the sudoke with a random puzzle"""
    # Unique row, unique column and unique square
    for row in range(0, 9):
        invalid = True
        while invalid:
            invalid = False
            clear_row(playing_field, row)
            for column in range(0, 9):
                allowed_values = list(range(1, 10))
                allowed_values = list(set(allowed_values) - set(get_horizontal_values(playing_field, column)))
                allowed_values = list(set(allowed_values) - set(get_vertical_values(playing_field, row)))
                try:
                    digit = random.choice(allowed_values)
                except(ValueError, IndexError):
                    invalid = True
                    break
                if ((is_duplicate_in_horizontal(digit, playing_field, column)) or (is_duplicate_in_vertical(digit, playing_field, row))) and not invalid:
                    invalid = True
                    break
                else:
                    fill_square(playing_field, column, row, digit)

    return playing_field

def clear_row(playing_field, y_coord):
    for column in range(0, 9):
        playing_field[y_coord][column] = 0

def get_horizontal_values(playing_field, x_coord):
    "Get the values of a horizontal colomn"
    horizontal_values = []
    for row in range(0, 9):
        horizontal_values.append(playing_field[row][x_coord])
    return horizontal_values

def is_duplicate_in_horizontal(digit, playing_field, x_coord):
    """Check if the number is a duplicate in the horizontal field"""
    return (digit in get_horizontal_values(playing_field, x_coord))

def get_vertical_values(playing_field, y_coord):
    "Get the values of a horizontal colomn"
    vertical_values = []
    for column in range(0, 9):
        vertical_values.append(playing_field[y_coord][column])
    return vertical_values

def is_duplicate_in_vertical(digit, playing_field, y_coord):
    """Check if the number is a duplicate in the vertical field"""
    return (digit in get_vertical_values(playing_field, y_coord))

def generate_pdf_of_playing_field(playing_field):
    """Generate a pdf of the playing field for visualisation"""
    # A4 dimensions are 210 mm x 297 mm
    pdf = FPDF('P', 'mm', 'A4')
    width = 210
    pdf.add_page()
    pdf.set_font('Arial', '', 26)
    square_side_size = 20
    offset_x = (width - (square_side_size*9))/2
    offset_y = 15

    for row in range(0, 9):
        pdf.set_y(offset_y + (square_side_size * (row)))
        pdf.set_x(offset_x)
        for column in range(0, 9):
            pdf.cell(square_side_size, square_side_size, str(playing_field[row][column]), 1, 0, 'C')

    line_width = 1.5
    pdf.set_line_width(line_width)

    for horizontal in range(0, 2):
        x_coord = offset_x + line_width/2
        y_coord = offset_y + ((horizontal+1)*square_side_size*3)
        pdf.line(x_coord, y_coord, width - x_coord, y_coord)

    for vertical in range(0, 2):
        x_coord = offset_y + ((vertical+1)*square_side_size*3)
        y_coord = offset_x + line_width/2
        pdf.line(x_coord, y_coord, x_coord, width - y_coord)

    pdf.output('sudoku.pdf', 'F')


def main():
    """Run the main program"""
    playing_field = fill_sudoku(create_empty_playing_field())
    print(playing_field)
    generate_pdf_of_playing_field(playing_field)

if __name__ == "__main__":
    main()
