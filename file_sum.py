# Author: Kristin Towns 
# GitHub username: kristinlashun
# Date: 2/7/2024
"""
This python function, file_sum, is designed to read a list of numbers from a specified text file, calculate the sum of these numbers, and then write the resulting 
sum to a new text file named 'sum.txt'. Each number in the input file is expected to be on a separate line. The function handles lines that cannot be converted to 
floats by ignoring them, ensuring that only valid numeric values contribute to the total sum. 
"""
def file_sum(filename): 
    total_sum = 0 
    with open(filename, 'r') as infile:
        for line in infile:
            try: 
                number = float(line)
                total_sum += number 
            except ValueError: 
                pass
    with open('sum.txt', 'w') as outfile: 
        outfile.write(str(total_sum))

        