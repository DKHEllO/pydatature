#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is about sorting and searching algorithms. The content of this document is mainly to explain and implement
# sequential search and binary search, selection sorting, bubble sorting, merge sorting, quick sorting, insert sorting,
# and shell sorting.And explain the idea of ​​hashing as a search technology. Using hash to implement Maps abstract data
# type

# binary search
def bin_search(find_list, num):
    """
    find a number in sorted list
    :param find_list: the found list
    :param num: the found number
    :return: bool(is it found),int(position)
    """
    start = 0
    end = len(find_list) - 1
    position = 0
    found = False
    while not found and start <= end:
        mid = (end + start) // 2
        if num < find_list[mid]:
            end = mid - 1
        elif num > find_list[mid]:
            start = mid + 1
        else:
            position = mid
            found = True
    return found, position

# Hash searching

# Hash table
# Hash tables are collections of items that are stored in a way that makes it easy to find them. Each position of the
# hash table, usually called a slot, can hold an item and is named by an integer value starting at 0.The mapping between
# the item and the slot to which the item belongs in the hash table is called the hash function. The hash function will
# receive any item in the collection and return an integer within the slot name range (between 0 and m-1).

# Hash function
# Given a set of items, the hash function that maps each item to a unique slot is called a perfect hash function.
"""
Group summation: Divide the items into equal-sized blocks (the last block may not be equal in size).Then add these blocks 
together to find the hash value. 
For example:
    if our item is a telephone number 436-555-4601, we will take the numbers and divide them into 2 digits (43, 65, 55, 46, 01). 
    43 + 65 + 55 + 46 + 01, we get 210. We assume that the hash table has 11 slots, then we need to divide by 11. In this case, 
    210% 11 is 1, so the phone number 436-555-4601 is hashed to slot 1.
"""

"""
Square to take the middle number(平方取中法)：We first squared the item and then extracted a part of the digital result
For example:
    If the item is 44, we will first calculate 44^2 = 1,936. By extracting the middle two numbers 93, we get 5 (93% 11)
"""

# Conflict resolution
# We are now back to the problem of collision. When two items are hashed to the same slot, we must have a systematic way
# to put the second item in the hash table. This process is called conflict resolution.

# rehash:Finding another slot after a conflict
"""
Open addressing:
Start with the original hash position and then move the slots sequentially until you encounter the first empty slot. 
Note that we may need to go back to the first slot (loop) to find the entire hash table. This conflict resolution 
process is called open addressing,By systematically visiting each slot at a time, we perform an open addressing 
technique called linear probing.

The disadvantage of linear detection is the tendency of aggregation, items are gathered in the table. This means that if
many collisions occur at the same hash value, multiple perimeter slots will be filled by linear probing. This will affect 
other items being inserted

extended linear detection
Instead of sequentially looking for the next open slot, skip the slots to more evenly distribute the items that have 
caused the conflict
"""

"""
Zipper method:
An alternative to dealing with conflicting issues is to allow each slot to hold a reference to a collection (or chain) 
of items. Links allow many items to exist in the same place in the hash table. When a conflict occurs, the item remains 
in the correct slot in the hash table. As more items are hashed into the same location, the difficulty of searching 
items in the collection increases
"""


class Map(object):
    def __init__(self, size):
        self.size = size
        self.solt = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)

        if self.solt[hash_value] == None:
            self.solt[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.solt[hash_value] == key:
                self.data[hash_value] = value
            else:
                # rehash
                next_hash = self.rehash(hash_value)
                # rehash until find a None solt or equal key solt
                while self.solt[next_hash] != None and self.solt[next_hash] != key:
                    next_hash = self.rehash(next_hash)
                # rpalce if key equal to key
                if self.solt[next_hash] == None:
                    self.solt[next_hash] = key
                    self.data[next_hash] = value
                else:
                    self.data[next_hash] = value

    def get(self, key):
        hash_value = self.hash_function(key)
        found = False
        stop = False
        data = None
        if self.solt[hash_value] == key:
            data = self.data[hash_value]
        else:
            next_hash = self.rehash(hash_value)
            while not found and self.solt[next_hash] != None and not stop:
                if self.solt[next_hash] == key:
                    found = True
                    data = self.data[next_hash]
                else:
                    next_hash = self.rehash(next_hash)
                    if next_hash == hash_value:
                        stop = True
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

# Loading factor
# a = Number of items/Number of solts
# The average number of times to find success
# aver = (summary of all items number of times to find success)/number of items
# The average number of times to find unsuccess
# 计算查找不成功的次数就直接找关键字到第一个地址上关键字为空的距离即可,然后计算所有查找的和再处以项数（即所有可能的情况）

# sorting


# Bubble Sort
def bubble_sort(num_list):
    l_len = len(num_list) - 1
    for i in range(l_len):
        for j in range(l_len-i):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j+1]
                num_list[j+1] = num_list[j]
                num_list[j] = temp
    return num_list


def short_bubble_sort(num_list):
    l_len = len(num_list) - 1
    for i in range(l_len):
        exchange = True
        for j in range(l_len-i):
            if num_list[j] > num_list[j+1]:
                exchange = False
                temp = num_list[j+1]
                num_list[j+1] = num_list[j]
                num_list[j] = temp
        if exchange:
            break
    return num_list

# select sort


def select_sort(num_list):
    l_len = len(num_list)-1
    for i in range(l_len+1):
        max_pos = 0
        for j in range(l_len-i+1):
            if num_list[j] > num_list[max_pos]:
                max_pos = j
        temp = num_list[l_len-i]
        num_list[l_len-i] = num_list[max_pos]
        num_list[max_pos] = temp
    return num_list



# insert sort


def insert_sort(num_list):
    for index in range(1, len(num_list)):
        current_value = num_list[index]
        position = index

        while position > 0 and num_list[position - 1] > current_value:
            num_list[position] = num_list[position - 1]
            position = position - 1

        num_list[position] = current_value



# quick sort


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


