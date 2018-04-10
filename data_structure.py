#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file define some basic data structures and does a simple implementation
# such as Queue,Stack,Deque,Linked list,Tree,Graph,Hash table


class Stack(object):
    """
    Create a empty stack
    items: storage elements in the stack
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Add a new item to the top of the stack
        :param item: The elements to add to the stack 
        :return: 
        """
        self.items.append(item)

    def pop(self):
        """
        Delete a new item to the top of the stack
        :return: 
        """
        return self.items.pop(-1)

    def is_empty(self):
        """
        Test stack is empty
        :return: True or False
        """
        return self.items == []

    def size(self):
        """
        Returns the number of items in the stack
        :return: int
        """
        return len(self.items)

    def peek(self):
        """
        Return to top item from stack
        :return: item(Undefined type, depending on the type of stack)
        """
        return self.items[-1]


class Queue(object):
    """
    Create a empty queue
    items: storage elements in the queue
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Add new items to the end of the queue
        :param item: The elements to add to the queue 
        :return: 
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove item from the header of queue and return 
        :return: item(Undefined type, depending on the type of queue)
        """
        item = self.items.pop(0)
        return item

    def is_empty(self):
        """
        Test stack is empty
        :return: True or Flase
        """
        return self.items == []

    def size(self):
        """
        Returns the number of items in the queue
        :return: 
        """
        return len(self.items)


class Deque(object):
    """
    Deque is an ordered collection of items that are similar to queues. It has two ends, a header and a tail, and the 
    items remain unchanged in the set. The difference with deque is that adding and deleting items is non-limiting. 
    You can add new items before or after. Similarly, existing items can be removed from either end. In a sense, this 
    hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.
    items: storage items in the deque
    """
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
        Add a new item to the deque's header
        :param item: The elements to add to the deque  
        :return: 
        """
        self.items.append(item)

    def add_rear(self, item):
        """
        Add a new item to the tail of deque
        :param item: The elements to add to the deque  
        :return: 
        """
        self.items.insert(0, item)

    def remove_front(self):
        """
        Delete a new item to the header of deque
        :return: 
        """
        self.items.pop(-1)

    def remove_rear(self):
        """
        Delete a new item to the tail of deque
        :return: 
        """
        self.items.pop(0)

    def size(self):
        """
        Returns the number of items in the deque
        :return: int
        """
        return len(self.items)

    def is_empty(self):
        """
        Test stack is empty
        :return: True or Flase
        """
        return self.items == []


class Node(object):
    """
    The basic structure of the linked list, each node object holds at least two information
    data: The data field of the node, the information of the node itself
    next: The reference to the next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """
        Return the data of the node itself
        :return: Uncertain type
        """
        return self.data

    def get_next(self):
        """
        Return the reference to the next node
        :return: Node
        """
        return self.next

    def set_data(self, data):
        """
        Modify the data of the node itself
        :param data: Modified data
        :return: 
        """
        self.data = data

    def set_next(self, node):
        """
        Modify the reference to the next node
        :param node: The next node to reference
        :return: 
        """
        self.next = node


class LinkedList(object):
    """
    Create a empty linked list. Linked list is built from a set of nodes, each of which is linked to the next node by an explicit reference. 
    As long as we know where to find the first node (including the first item), each subsequent item can be found by 
    following the next link in succession.
    head: Linked list of head references    
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Test stack is empty
        :return: False or True
        """
        return self.head == None

    def add(self, item):
        """
        Add a node to the linked list
        :param item: The elements to add to the linked list 
        :return: 
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        Returns the number of nodes in the linked list
        :return: int
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        """
        Finding the specified node in the linked list
        :param item: The node to find
        :return: Node
        """
        current = self.head
        while current!=None:
            if current.data == item:
                break
            else:
                current = current.get_next()
        return current

    def remove(self, item):
        """
        Removing the specified node in the linked list
        :param item: The node to remove
        :return: True or False
        """
        current = self.head
        previous = None
        found = False
        while current!=None:
            if current.data == item:
                found = True
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    self.head = previous
                break
            else:
                current = current.get_next()
                previous = current
        return found


class OrderedList(object):
    """
    Create a ordered linked list
    """
    def __init__(self):
        pass


class BinaryTree(object):
    """
    Create a binary tree object with root node and left and right subtrees 
    root: The root object of the tree, can be a reference to any object
    left_child: The reference to the tree's left subtree
    right_child: The reference to the tree's right subtree
    """
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, node):
        """
        Insert a left subtree to the tree
        :param node: The reference to the tree
        :return: 
        """
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right_child(self, node):
        """
        Insert a right subtree to the tree
        :param node: The reference to the tree
        :return: 
        """
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_right_child(self):
        """
        Return the reference of right subtree
        :return: any object
        """
        return self.right_child

    def get_left_child(self):
        """
        Return the reference of left subtree
        :return: Object
        """
        return self.left_child

    def get_root_val(self):
        """
        Return the root object
        :return: Object
        """
        return self.root

    def set_root_val(self, root_obj):
        """
        Modify the root object
        :param root_obj: Modified object
        :return: 
        """
        self.root = root_obj


class Vertex(object):
    """
    Create a vertex of graph, each vertex has an id and a dictionary that tracks the vertices it connects to and the 
    weight of each edge
    id: The vertex's id
    connected_to: Trace the dictionary of connections and weights
    """
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])

    def __init__(self, id):
        self.id = id
        self.connected_to = {}

    def add_nbr(self, nbr, weight=0):
        """
        Add a connection to another vertex
        :param nbr: The vertex to connect
        :param weight: The weight of edge
        :return: 
        """
        self.connected_to[nbr] = weight

    def get_connections(self):
        """
        Return all vertices in the adjacency table
        :return: list
        """
        return self.connected_to.keys()

    def get_id(self):
        """
        Return the vertex's id
        :return: Uncertain type
        """
        return self.id

    def get_weight(self, nbr):
        """
        Return the weight of the edge to another vertex
        :param nbr: The specified vertex
        :return: int
        """
        return self.connected_to[nbr]


class Graph(object):
    """
    The list to save vertices
    vtx_list: The list to storage all vertexs
    num_vtx: The number of vertexs in the list
    """
    def __init__(self):
        self.vtx_list = {}
        self.num_vtx = 0

    def __iter__(self):
        return iter(self.vtx_list.values())

    def __contains__(self, n):
        return n in self.vtx_list

    def add_vtx(self, key):
        """
        Add a vertex to the graph
        :param key: The added vertex id
        :return: 
        """
        self.num_vtx += 1
        new_vtx = Vertex(key)
        self.vtx_list[key] = new_vtx

    def get_vtx(self, key):
        """
        Return the specified vertex reference
        :param key: The specified vertex id
        :return: Vertex or None
        """
        if key in self.vtx_list:
            return self.vtx_list[key]
        else:
            return None

    def add_edge(self, s, e, cost=0):
        """
        Add an edge to the graph
        :param s: The start vertex of edge
        :param e: The end vertex of edge
        :param cost: The edge's weight
        :return: 
        """
        if s not in self.vtx_list:
            self.add_vtx(s)
        if e not in self.vtx_list:
            self.add_vtx(e)
        self.vtx_list[s].add_nbr(self.vtx_list[e], cost)

    def get_vtxs(self):
        """
        Return all vertexs from the graph
        :return: list of Vertex
        """
        return self.vtx_list.keys()


# Binary Heap
"""
    The heap looks like a tree, but when we implement it, we use only a single list as an internal representation. The 
    binary heap has two common variants: the smallest heap (where the smallest key is always in front) and the largest 
    heap (where the largest key is always in front)
    
    In order for our heap to work effectively, we will use the logarithmic nature of the binary tree to represent our 
    heap. In order to ensure logarithmic performance, we must keep the balance of the tree. The balanced binary tree 
    has roughly the same number of nodes in the left and right subtrees of the root. In our heap implementation, we 
    maintain the balance of the tree by creating a complete binary tree. A complete binary tree is a tree, where each 
    layer has all its nodes, except for the lowest level of the tree, filled from left to right.Another interesting 
    property of a complete binary tree is that we can use a single list to represent it. We don't need to use nodes 
    and references, or even lists of lists. Because the tree is complete, the parent's left child (at position p) is 
    the node found in position 2p in the list. Similarly, the position of the right child of the parent node in the 
    list 2p + 1
    
    The heap's sorting properties are as follows: In the heap, for each node x with a parent p, the key in p is less 
    than or equal to the key in x
"""
# Smallest Heap


class SmallestHeap(object):
    """ 
    Smallest Heap: where the smallest key is always in front
    heap_list: The entire binary heap is represented by a single list. An empty binary heap has a single zero. This zero 
    is used for simple integer division later.
    size: Binary heap size
    """
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, k):
        """
        insert a value to binary heap
        :param k: the specified value
        :return: 
        """
        self.size += 1
        self.heap_list.append(k)
        i = self.size
        while i//2:
            if self.heap_list[i] < self.heap_list[i//2]:
                temp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i//2] = temp
            i = i//2

    def find_min(self, i):
        """
        Find the smallest subtree position of specified position   
        :param i: specified position
        :return: int(smallest subtree position)
        """
        if i * 2 + 1 > self.size:
            return i * 2 + 1
        else:
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2

    def del_min(self):
        """
        Del the smallest value in the binary heap, fill the last value to the root after del the smallest value to keep 
        our heap structure. Then restore heap order by pushing the new root node down the tree to its correct position. 
        :return: None
        """
        tail = self.heap_list.pop()
        self.size -= 1
        self.heap_list[1] = tail
        i = 1
        while i*2 <= self.size:
            min_pos = self.find_min(i)
            if self.heap_list[min_pos] < self.heap_list[i]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_pos]
                self.heap_list[min_pos] = temp
            i = min_pos

    def is_empty(self):
        """
        Return the heap is empty
        :return: False or True 
        """
        return self.heap_list == [0]

    def size(self):
        """
        Return size of heap
        :return: int
        """
        return self.size

    def build_list(self, new_list):
        """
        Build a smallest heap from specified list
        :param new_list: specified list
        :return: 
        """
        list_len = len(new_list)
        self.size = list_len
        i = list_len // 2
        self.heap_list = [0] + new_list
        while i > 0:
            min_pos = self.find_min(i)
            if self.heap_list[min_pos] < self.heap_list[i]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_pos]
                self.heap_list[min_pos] = temp
            i = i - 1


# Largest Heap


class LargestHeap(object):
    """ 
    Largest Heap: where the largest key is always in front
    heap_list: The entire binary heap is represented by a single list. An empty binary heap has a single zero. This zero 
    is used for simple integer division later.
    size: Binary heap size
    """
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def insert(self, k):
        """
        insert a value to binary heap
        :param k: the specified value
        :return: 
        """
        self.size += 1
        self.heap_list.append(k)
        i = self.size
        if i == 1:
            pass
        else:
            while i//2:
                if self.heap_list[i] > self.heap_list[i//2]:
                    temp = self.heap_list[i//2]
                    self.heap_list[i//2] = self.heap_list[i]
                    self.heap_list[i//2] = temp
                i = i//2

    def find_max(self, i):
        """
        Find the largest subtree position of specified position   
        :param i: specified position
        :return: int(smallest subtree position)
        """
        if i * 2 + 1 > self.size:
            return i * 2 + 1
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2

    def del_max(self):
        """
        Del the largest value in the binary heap, fill the last value to the root after del the largest value to keep 
        our heap structure. Then restore heap order by pushing the new root node down the tree to its correct position. 
        :return: None
        """
        tail = self.heap_list.pop()
        self.size -= 1
        self.heap_list[1] = tail
        i = 1
        while i*2 <= self.size:
            max_pos = self.find_max(i)
            if self.heap_list[max_pos] > self.heap_list[i]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[max_pos]
                self.heap_list[max_pos] = temp
            i = max_pos

    def is_empty(self):
        """
        Return the heap is empty
        :return: False or True 
        """
        return self.heap_list == [0]

    def size(self):
        """
        Return size of heap
        :return: int
        """
        return self.size

    def build_list(self, new_list):
        """
        Build a largest heap from specified list
        :param new_list: specified list
        :return: 
        """
        list_len = len(new_list)
        self.size = list_len
        i = list_len // 2
        self.heap_list = [0] + new_list
        while i > 0:
            max_pos = self.find_max(i)
            if self.heap_list[max_pos] > self.heap_list[i]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[max_pos]
                self.heap_list[max_pos] = temp
            i = i - 1













