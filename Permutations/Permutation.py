import sys
import os


def GetItem(list):
    if len(list) == 1:
        return [list]
    else:
        return list

def ListPermutation (list):
    if len(list) == 1:
        return list
    else :
        first = list.pop(0)
        remaining_list = ListPermutation(list)

        list_of_lists = []

        for sub_list in remaining_list:
            new_list = GetItem(sub_list)

            for j in range(0, len(new_list) + 1):
                new_list.insert(j, first)
                list_of_lists.insert(0, new_list.copy())
                new_list.remove(first)

        return list_of_lists

print('Enter a postive number: ')
input_number = sys.stdin.readline()
input_list = []

if (int(input_number) > 0):
    for i in range(0, int(input_number)):
        input_list.append(chr(i + ord('a')))

    print('Input list: ', input_list)

    i = 1
    new_list = ListPermutation(input_list)
    new_list.sort()

    output_file = open("permutation.txt", "wb")

    for item in new_list:
        string = str.format("%(Number)3d: %(item)s\n" % {'Number': i, 'item': item})
        output_file.write(bytes(string, 'UTF-8'))
        i += 1

    output_file.close()
else:
    print('Bad input')
