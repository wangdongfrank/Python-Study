#!/usr/bin/env python

def swap(data_list, i1, i2):
    temp = data_list[i1]
    data_list[i1] = data_list[i2]
    data_list[i2] = temp

def bubble_sort(data_list):
    flag = True
    for i in range( 1, len(data_list)):
        flag = True
        for j in range( 1, len(data_list)):
            if data_list[j-1] > data_list[j]:
                flag = False
                swap(data_list, j, j-1)
                print data_list

        if flag:
            break

def selection_sort(data_list):
    for i in range( len(data_list)-1):
        for j in range( i+1, len(data_list)):
            if data_list[j] < data_list[i]:
                swap(data_list, i, j)
                print data_list

def insertion_sort(data_list):
    for i in range( len(data_list) ):
        temp = data_list[i]
        k = i
        while data_list[k-1] > temp and k > 0:
            data_list[k] = data_list[k-1]
            k -= 1
        data_list[k] = temp
        print data_list

def merge_sort(data_list, low, high):
    if low < high:
        middle = (low + high) / 2
        merge_sort(data_list, low, middle)
        merge_sort(data_list, middle+1, high)
        merge(data_list, low, middle, high)

def merge(data_list, low, middle, high):
    helper = [None] * len(data_list)
    for i in range(low, high+1):
        helper[i] = data_list[i]

    helper_left = low
    helper_right = middle + 1
    current = low

    while helper_left <= middle and helper_right <= high:
        if helper[helper_left] <= helper[helper_right]:
            data_list[current] = helper[helper_left]
            helper_left += 1
        else:
            data_list[current] = helper[helper_right]
            helper_right += 1
        current += 1

    remaining = middle - helper_left
    for i in range(remaining+1):
        data_list[current+i] = helper[helper_left+i]


# These are all for quick sort
def quick_sort(data_list, left, right):
    index = partition(data_list, left, right)

    if left < index - 1:
        quick_sort(data_list, left, index - 1)

    if index < right:
        quick_sort(data_list, index, right)

def partition(data_list, left, right):
    pivot = data_list[ (left + right ) / 2]

    while left < right:
        while data_list[left] < pivot:
            left += 1
        while data_list[right] > pivot:
            right -= 1
        if left <= right:
            swap(data_list, left, right)
            left += 1
            right -= 1

    return left

# Maybe heapsort

# Binary Search
def binary_search_recur(data_list, i, low, high):
    mid = (low + high) / 2
    if i == data_list[mid]:
        return True
    elif i < data_list[mid]:
        return binary_search_recur(data_list, i, low, mid-1)
    else:
        return binary_search_recur(data_list, i, mid+1, high)
    return False

def binary_search_iter(data_list, i):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) / 2
        if i == data_list[mid]:
            return True
        elif i < data_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
        print low, mid, high

    return False

# Q1 len(list_a) is much larger than len(list_b)
def merge_lists(list_a, list_b):
    index_a = len(list_a) - 1
    index_b = len(list_b) - 1
    current = index_a + index_b + 1
    while index_a > 0 and index_b > 0:
        if list_a[index_a] <= list_b[index_b]:
            index_a[current] = list_b[index_b]
            index_b -= 1
            current -=1
        else:
            index_a[current] = list_a[index_a]
            index_a -= 1
            current -= 1
    if index_b > 0:
        for i in range(current+1):
            list_a[current] = list_b[current]

# Q2
def sort_anagrams(ana_list):
    pass

# Q3
def find_rotate(data_list, i):
    pass

# Q5
def search_empty_string(data_list, i):
    pass


if __name__ == '__main__':
    import random
    data_list = []
    while True:
        rand = random.randint(0,20)
        if rand not in data_list:
            data_list.append(rand)
            if len(data_list) == 21:
                break
    print data_list
    #selection_sort(data_list)
    #bubble_sort(data_list)
    #insertion_sort(data_list)
    #merge_sort(data_list, 0, len(data_list)-1)
    #quick_sort(data_list, 0, len(data_list)-1)
    #print binary_search_recur(data_list, 10, 0, len(data_list)-1)
    print binary_search_iter(data_list, 10)
