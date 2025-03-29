class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if the number of rows is 1 or greater than or equal to the length of the string
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array to store strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            # Add the current character to the current row
            rows[current_row] += char

            # If we're at the top or bottom row, switch direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row in the current direction
            current_row += 1 if going_down else -1

        # Concatenate all rows to get the final result
        return ''.join(rows)