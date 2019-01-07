import sys

cursor_line_number = 130
last_method_name = None
lastBlock = ''
saw_is_test = False
about_to_see_method_name = False
parent_method_name = ''

with open("output.txt", "r") as f:

    for line in f:
        components = line.split()
        current_line_number = components[0].split(',')[0]
        currentBlock = components[2]

        if lastBlock == "'@'" and currentBlock == "'isTest'":
            saw_is_test = True
        lastBlock = currentBlock

        if saw_is_test and currentBlock == "'void'":
            about_to_see_method_name = True
            saw_is_test = False
        elif not saw_is_test and about_to_see_method_name:
            about_to_see_method_name = False
            last_method_name = currentBlock

        if int(current_line_number) < cursor_line_number:
            parent_method_name = last_method_name

f.close()
print parent_method_name
