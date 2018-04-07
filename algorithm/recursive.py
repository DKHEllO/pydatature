#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Recursion is a method of solving the problem. It breaks the problem down into smaller sub-problems until a sufficiently
# small problem can be solved simply. Usually recursively involves the function call itself. Recursion allows us to write
# elegant solutions that solve problems that may be difficult to program.

# simple example
# Calculate integer sums

# normal
def listsum_normal(numList):
    """
    :param numList: 
    :return: 
    """
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

# recursion
def listsum_recursion(numList):
    """
    :param numList: 
    :return: 
    """
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum_recursion(numList[1:])

# Each time we make a recursive call, we will solve a smaller problem until the problem cannot be reduced. When we arrive
# at the point of simple questions, we begin to piece together the answers to each small question until the initial problem
# is solved.

# Like Asimov robots, all recursive algorithms must obey three important laws:
# Recursive algorithms must have basic conditions.
# The recursive algorithm must change its state and approach the basic situation.
# The recursive algorithm must call itself recursively.

# Integer converted to an arbitrary string


def int_2_str(n, base):
    """
    transfer int to arbitrary str
    :param n: the tranfered number
    :param base: system
    :return: 
    """
    base_str = "0123456789ABCDEF"
    if n < base:
        return base_str[n]
    else:
        return int_2_str(n//base, base) + base_str[n % base]

# How Python implements a recursive function call
# When calling a function in Python, a stack is allocated to handle the function's local variables. When the function
# returns, the return value is left at the top of the stack for access by the calling function
# The stack frame also provides a scope for the variables used by the function. Even if we repeatedly call the same
# function, each call creates a new scope for the function's local variables.

# Sherbinski triangle(twice)
#            /\
#           /  \
#          /____\
#         /\    /\
#        /  \  /  \
#       /____\/____\
#      /\    /\    /\
#     /  \  /  \  /  \
#    /____\/____\/____\
#   /\    /\    /\    /\
#  /  \  /  \  /  \  /  \
# /____\/____\/____\/____\


def sherb_triangle(points, triangle_dic, n):
    """
    :param points: triangle's points list(top, left, right) 
    :param triangle_dic: store triangles that each split   
    :param n: split times
    :return: triangle_dic
    """
    if n < 1:
        return
    else:
        triangle_dic.setdefault(n, [])
        triangle_dic[n].append(points)
        mid_top_left = [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2]
        mid_top_right = [(points[0][0] + points[2][0]) / 2, (points[0][1] + points[2][1]) / 2]
        mid_left_right = [(points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2]
        sherb_triangle([mid_top_left, points[1], mid_left_right], triangle_dic, n-1)
        sherb_triangle([points[0], mid_top_left, mid_top_right], triangle_dic, n-1)
        sherb_triangle([mid_left_right, mid_left_right, points[2]], triangle_dic, n-1)
        return triangle_dic


# **********************************************************************************************************************
# Hanoi Tower Games
# Tower of Hanoi was invented by the French mathematician Edward Lucas in 1883. His inspiration comes from a legend
# that has a Hindu temple that gives the young pastor a puzzle. At the beginning, the priests were given three poles and
# a pile of 64 gold discs, each one smaller than the one below it. Their task is to transfer all 64 dishes from one of
# three bars to another. There are two important constraints, they can only move one plate at a time, and they cannot
# place larger plates on top of smaller plates. The priest keeps moving a plate every second day and night. When they
# completed their work, it was said that the temples would become dust and the world would disappear.

# Here's how to use the middle lever to move the tower from the start rod to the target rod:
# 1、Use the target rod to move the height-1 tower to the middle rod.
# 2、Move start rod's tower to target rod.
# 3、Use the start rod to move the height-1 tower to the target rod.


def move_tower(height, from_pole, to_pole, with_pole):
    """
    :param height: the height of Hanoi tower 
    :param from_pole: start pole position
    :param to_pole: end pole position
    :param with_pole: middle pole position
    :return: the method
    """
    if height >= 1:
        if height > 2:
            print "-"*(height-1) + "move %s from %s to %s with %s" % (height-1, from_pole, with_pole, to_pole)
        move_tower(height-1, from_pole, with_pole, to_pole)
        if height == 2:
            print "moving disk from", from_pole, "to", to_pole
        else:
            print"-"*(height-1) + "moving disk from", from_pole, "to", to_pole
        if height > 2:
            print "-"*(height-1) + "move %s from %s to %s with %s" % (height-1, with_pole, to_pole, from_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

# move_tower(5, 1, 3, 2)

# **********************************************************************************************************************


# Dynamic planning
# Many programs in computer science are written to optimize some values; for example, finding the shortest path between
# two points, finding the line that best fits a set of points, or finding the smallest set of objects that meet certain
# criteria. Computer scientists use many strategies to solve these problems. Dynamic planning is a strategy for these
# types of optimization problems

# coin change
# A truly dynamic programming algorithm will take a more systematic approach to solving this problem. Our dynamic
# programming solution will start with finding a penny and systematically find the amount of change we need. This
# ensures that at every step of the algorithm we already know the minimum number of coins needed to make a change
# for any smaller quantity.
# this method create a change table, each item corresponds the least amount of change, every change only to use all
# possible coins to change the specified amount. find the number of coins remaining in the change table, and then
# compare all possible cases to find the smallest

def coin_change(coin_list, change):
    """
    :param coin_list: coins that can be used 
    :param change: 
    :return: min_coin_list(the minimum number of coins used in all case), min_change_list(coins that be used in all case)
    """
    min_coin_list = [0]
    min_change_list = [[]]
    for i in range(1, change+1):
        coin_num = i
        for j in [c for c in coin_list if c <= i]:
            change_list = []
            if min_coin_list[i - j] + 1 < coin_num:
                coin_num = min_coin_list[i-j] + 1
                change_list = [j] + min_change_list[i-j]
            else:
                change_list += [j] + min_change_list[i-j]
        min_coin_list.append(coin_num)
        min_change_list.append(change_list)
    return min_coin_list, min_change_list

# summary
# Recursive algorithms usually map naturally to the expressions of the problem you are trying to solve
# Recursion is not always the answer. At times, recursive solutions may be computationally more expensive than iterative
# algorithms



