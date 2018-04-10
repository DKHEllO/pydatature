#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Analysis Tree

from data_structure import Stack, BinaryTree


def build_prase_tree(expression):
    ex_list = list(expression)
    stack = Stack()
    bin_tree = BinaryTree('root')
    for i in ex_list:
        if i == '(':
            stack.push(bin_tree)
            bin_tree.insert_left_child('-')
            bin_tree = bin_tree.left_child
        elif i in '+-*/':
            bin_tree = stack.pop()
            bin_tree.set_root_val(i)
            bin_tree.insert_right_child('')
            stack.push(bin_tree)
            bin_tree = bin_tree.right_child
        elif i == ')':
            bin_tree = stack.pop()
        elif i not in '+-*/':
            bin_tree.set_root_val(i)
        else:
            raise ValueError
    return bin_tree


# Preorder traversal
# root left right

def preorder_trav(tree):
    if tree:
        print tree.get_root_val()
        preorder_trav(tree.left_child)
        preorder_trav(tree.right_child)


# In Order traversal
# left root right
def order_trav(tree):
    if tree:
        order_trav(tree.left_child)
        print tree.get_root_val
        order_trav(tree.right_child)


# Postorder traversal
# left right root
def postorder_trav(tree):
    if tree:
        postorder_trav(tree.left_child)
        postorder_trav(tree.right_child)
        print tree.get_root_val