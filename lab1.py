"""
Please open file "lab1_file.txt" to see the file structure.
The first line of the file indicates how many data lines in the file, say n.
The following n lines are the data lines, each line has a number.

The program reads the file "lab1_file.txt", and calculate average number of all those data line.
"""


def computer_average(filename):
    file_obj = open(filename, "r")
   

    # read file line, which is number of lines
    first_line = file_obj.readline()
    nums_line = int(first_line)

    # create a list to wrap all following numbers
    numbers = []

    for i in range(nums_line):
        num = float(file_obj.readline())
        numbers.append(num)

    file_obj.close()

    avg = sum(numbers) / len(numbers)
    return avg


if __name__ == "__main__":
    average = computer_average("lab1_file.txt")
    print(average)
