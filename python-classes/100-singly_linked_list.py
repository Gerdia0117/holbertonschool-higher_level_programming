#!/usr/bin/python3
"""Defines classes for a singly linked list: Node and SinglyLinkedList.
"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): data stored in the node
            next_node (Node): reference to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list that is always sorted."""

    def __init__(self):
        """Initialize an empty linked list"""
        self.__head = None

    def __str__(self):
        """Return string representation of the list (one node per line)."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the list in the correct sorted position.
        Args:
            value (int): data to insert into the new node
        """
        new_node = Node(value)

        # If the list is empty or new_node should be first
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse to find the insertion point
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
