from typing import *
import enum

board = [
    '1  3  3 1 2 3',
    '     2 3 3 3 ',
    '4  4        2',
    '     4  1  2 ',
    ' 2     3    4',
    '3  3     3 3 ',
    ' 3        1 1',
    '3    4 5 5 2 ',
    ' 4 3      3 3',
    '3     2  3 2 ',
    ' 4   2 3  4 4',
    '3            ',
    ' 4  4 6  3 1 ',
    '3    1  1   3',
    ' 4 1  2  2 3 ',
    '3 1 3     1 1',
    ' 3   5  4  3 ',
    '3 3 3 3  3  2'
]
# 1 = ─
# 2 = ═
# 3 = │
# 4 = ║
edges = [
    '             ',
    '3  3         ',
    ' 22          ',
    '3            ',
    '3            ',
    ' 4           ',
    '4            ',
    '             ',
    '             ',
    '             ',
    '             ',
    '             ',
    '             ',
    '             ',
    '             ',
    '             ',
    '  222        ',
    '             '
]

class Size(enum.Enum):
    Small = 1
    Medium = 2
    Large = 3

class EdgeChar(enum.Enum):
    # 1 = ─
    # 2 = ═
    # 3 = │
    # 4 = ║
    Horiz = '─'
    DoubHoriz = '═'
    Vert = '│'
    DoubVert = '║'

def main():
    print()
    print_board(board, edges, Size.Large)
    print_board(board, edges, Size.Medium)
    print_board(board, edges, Size.Small)

def print_board(board, edges=None, size: Size = Size.Large):
    if len(board) == 0 or len(board[0]) == 0:
        raise ValueError('Error: board has 0 width or 0 height')

    height = len(board)
    width = len(board[0])

    if edges is None:
        edges = [' ' * width] * height

    # Choose how to print based on Size
    all_printable_lines = []
    if size == Size.Small:
        # Add first line
        all_printable_lines.append('┌' + EdgeChar.Horiz.value*(width+2) + '┐')

        for row in range(height):
            line = '│ '

            for col in range(width):
                if edges[row][col] != ' ':
                    # 1 = ─
                    # 2 = ═
                    # 3 = │
                    # 4 = ║
                    if edges[row][col] == '1':
                        line += EdgeChar.Horiz.value
                    elif edges[row][col] == '2':
                        line += EdgeChar.DoubHoriz.value
                    elif edges[row][col] == '3':
                        line += EdgeChar.Vert.value
                    elif edges[row][col] == '4':
                        line += EdgeChar.DoubVert.value
                    else:
                        raise ValueError(f'Error: edges[{row}][{col}] invalid: {edges[row][col]}')
                else:
                    line += board[row][col]

            line += f' {EdgeChar.Vert.value}'
            all_printable_lines.append(line)

        # Add final line
        all_printable_lines.append('└' + EdgeChar.Horiz.value*(width+2) + '┘')
    elif size == Size.Medium:
        # Width of printed board area
        # Each cell is 3 wide, +2 for 1 space padding on L+R 
        printed_width = 3 * width + 2

        # Add first line
        all_printable_lines.append('┌' + EdgeChar.Horiz.value*printed_width + '┐')

        for row in range(height):
            # Each row in board will be 3 lines tall printed
            line = f'{EdgeChar.Vert.value} '

            for col in range(width):
                # Add to lines for this cell
                if edges[row][col] != ' ':
                    # Add this edge
                    if edges[row][col] == '1':
                        line += EdgeChar.Horiz.value * 3
                    elif edges[row][col] == '2':
                        line += EdgeChar.DoubHoriz.value * 3
                    elif edges[row][col] == '3':
                        line += f' {EdgeChar.Vert.value} '
                    elif edges[row][col] == '4':
                        line += f' {EdgeChar.DoubVert.value} '
                    else:
                        raise ValueError(f'Error: edges[{row}][{col}] invalid: {edges[row][col]}')
                elif board[row][col] != ' ':
                    # Add this cell
                    line += f' {board[row][col]} '
                else:
                    # Add blank cell
                    line += ' ' * 3
            # Add end of line
            line += f' {EdgeChar.Vert.value}'

            all_printable_lines.append(line)

        # Add final line
        all_printable_lines.append('└' + '─'*printed_width + '┘')
    elif size == Size.Large:
        # Width of printed board area
        # Each cell is 5 wide, + 1 for each gap between cells, 
        # +2 for 1 space padding on L+R 
        # ie. (5*width) + (width-1) + 2 = \/
        printed_width = 6 * width + 1

        # Add first line
        all_printable_lines.append('┌' + EdgeChar.Horiz.value*printed_width + '┐')

        for row in range(height):
            # Each row in board will be 3 lines tall printed
            l1 = f'{EdgeChar.Vert.value} '
            l2 = f'{EdgeChar.Vert.value} '
            l3 = f'{EdgeChar.Vert.value} '

            for col in range(width):
                # Fill the 1-char gap between this cell and the last
                if col != 0:
                    if edges[row][col] == '1' or edges[row][col-1] == '1':
                        l1 += ' '
                        l2 += EdgeChar.Horiz.value
                        l3 += ' '
                    elif edges[row][col] == '2' or edges[row][col-1] == '2':
                        l1 += ' '
                        l2 += EdgeChar.DoubHoriz.value
                        l3 += ' '
                    else:
                        l1 += ' '
                        l2 += ' '
                        l3 += ' '

                # Add to lines for this cell
                if edges[row][col] != ' ':
                    # Add this edge
                    if edges[row][col] == '1':
                        l1 += ' ' * 5
                        l2 += EdgeChar.Horiz.value * 5
                        l3 += ' ' * 5
                    elif edges[row][col] == '2':
                        l1 += ' ' * 5
                        l2 += EdgeChar.DoubHoriz.value * 5
                        l3 += ' ' * 5
                    elif edges[row][col] == '3':
                        l1 += f'  {EdgeChar.Vert.value}  '
                        l2 += f'  {EdgeChar.Vert.value}  '
                        l3 += f'  {EdgeChar.Vert.value}  '
                    elif edges[row][col] == '4':
                        l1 += f'  {EdgeChar.DoubVert.value}  '
                        l2 += f'  {EdgeChar.DoubVert.value}  '
                        l3 += f'  {EdgeChar.DoubVert.value}  '
                    else:
                        raise ValueError(f'Error: edges[{row}][{col}] invalid: {edges[row][col]}')
                elif board[row][col] != ' ':
                    # Add this cell
                    l1 += '┏━━━┓'
                    l2 += f'┃ {board[row][col]} ┃'
                    l3 += '┗━━━┛'
                else:
                    # Add blank cell
                    l1 += ' ' * 5
                    l2 += ' ' * 5
                    l3 += ' ' * 5
            # Add end of line
            l1 += f' {EdgeChar.Vert.value}'
            l2 += f' {EdgeChar.Vert.value}'
            l3 += f' {EdgeChar.Vert.value}'

            all_printable_lines.extend([l1, l2, l3])

        # Add final line
        all_printable_lines.append('└' + '─'*printed_width + '┘')
    else:
        raise ValueError('Error: Size not supported')

    for line in all_printable_lines:
        print(line)


main()