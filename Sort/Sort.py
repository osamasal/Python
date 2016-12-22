import random
import sys
import datetime


def BubbleSort(list):
    changed = 1

    while changed == 1:
        changed = 0

        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i]=list[i + 1]
                list[i + 1]=temp
                changed = 1

    return list

#################################################################

def SelectionSort(list):
    for current_element_index in range(0, len(list)):

        for i in range(current_element_index + 1, len(list)):
            if list[current_element_index] > list[i]:
                temp = list[current_element_index]
                list[current_element_index] = list[i]
                list[i] = temp

    return list

#################################################################

def SplitList(list, start, end):
    tempList = []

    for i in range(start, end):
        tempList.append(list[i])

    return tempList

def MergeSort(list):
    firstHalf = SplitList(list, 0, len(list) // 2)
    secondHalf = SplitList(list, len(list) // 2, len(list))

    if len(firstHalf) <= 1 and len(secondHalf) <= 1:
        return Merge(firstHalf, secondHalf)
    else:
        return Merge(MergeSort(firstHalf), MergeSort(secondHalf))

def Merge(first_list, second_list):
    first_list_index = 0
    second_list_index = 0
    resulting_list  = []

    while first_list_index < len(first_list) and second_list_index < len(second_list):
        if (first_list[first_list_index] < second_list[second_list_index]):
            resulting_list.append(first_list[first_list_index])
            first_list_index += 1
        else:
            resulting_list.append(second_list[second_list_index])
            second_list_index += 1

    while first_list_index < len(first_list):
        resulting_list.append(first_list[first_list_index])
        first_list_index += 1

    while second_list_index < len(second_list):
        resulting_list.append(second_list[second_list_index])
        second_list_index += 1

    return resulting_list

print('Enter a postive number: ')
input_number = sys.stdin.readline()
input_list = []

if (int(input_number) > 0):
    for i in range(0, int(input_number)):
        input_list.append(random.randrange(-10000, 10000))

    start_time = datetime.datetime.now().microsecond
    print('Unsorted:\t\t', input_list)
    print('Bubble sort:\t', BubbleSort(input_list.copy()))
    print(datetime.datetime.now().microsecond - start_time, 'microseconds')
    start_time = datetime.datetime.now().microsecond
    print('Selection sort:\t', SelectionSort(input_list.copy()))
    print(datetime.datetime.now().microsecond - start_time, 'microseconds')
    start_time = datetime.datetime.now().microsecond
    print('Merge sort:\t\t', MergeSort(input_list.copy()))
    print(datetime.datetime.now().microsecond - start_time, 'microseconds')
else:
    print('Bad input')
