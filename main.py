# pylint: disable=W0104, line-too-long
"""Give the answer of a sudoku puzzle"""
import random

def create_empty_playing_field():
    """Create an empty playing field"""
    playing_field = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return playing_field

def fill_square(playing_field, x_coord, y_coord, value):
    """Fill a square with a number"""
    playing_field[y_coord][x_coord] = int(value)

def generate_completed_sudoku(playing_field):
    """Fill the sudoke with a random puzzle"""
    for row in range(0, 9):
        for column in range(0, 9):
            horizontal_values = get_horizontal_values(playing_field, column)
            vertical_values = get_vertical_values(playing_field, row)
            allowedvalues = list(range(1, 10))
            while 1:
                digit = random.choice(allowedvalues)
                if (digit not in horizontal_values) and (digit not in vertical_values):
                    break
                allowedvalues.remove(digit)
            fill_square(playing_field, column, row, digit)
    return playing_field


def get_horizontal_values(playing_field, x_coord):
    "Get the values of a horizontal colomn"
    horizontal_values = []
    for row in range(0, 9):
        horizontal_values.append(playing_field[row][x_coord])
    return horizontal_values

def get_vertical_values(playing_field, y_coord):
    "Get the values of a horizontal colomn"
    vertical_values = []
    for column in range(0, 9):
        vertical_values.append(playing_field[y_coord][column])
    return vertical_values

def main():
    """Run the main program"""
    playing_field = generate_completed_sudoku(create_empty_playing_field())
    print(playing_field)

if __name__ == "__main__":
    # execute only if run as a script
    main()
