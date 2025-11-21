file_obj = open("data1.txt", "r")
content = file_obj.read()

# You would see the entire poem "The zen of python"
# You can open the file "data1.txt" to see it.
print(content)

# Remember to close the file after file manipulation
file_obj.close()