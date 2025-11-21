"""
Please open the file "lab2_file.txt" to see its structure.
It has the following structure:
    Pink,85
    Red,44
    Maroon,80

File "lab2_file.txt" records the number of paint bottles bought within a year,
every line has two fields: the color of the paint, and the number of bottles,
and they are separated by a comma (,)

This program is used to count the number of bottles for each color,
and write the final result into a new file.
"""


def count_paint_bottles(input_file, output_file):
    totals = {}

    file_obj = open(input_file, "r")

    for line in file_obj:
        fields = line.strip().split(",")
        color = fields[0]
        num = int(fields[1])

        if color not in totals:
            totals[color] = num
        else:
           totals[color] += num

    file_obj.close()


    file_obj2 = open(output_file, "w")

    for color in totals.keys():
        num_str = str(totals[color])
        string_to_write = color + ":" + num_str # comebine the string

        file_obj2.write(string_to_write)
        file_obj2.write("\n")

    file_obj2.close()


if __name__ == "__main__":
    count_paint_bottles("lab2_file.txt", "lab2_result.txt")
