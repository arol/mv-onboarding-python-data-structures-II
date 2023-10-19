import pytest
from src.linked_list import LinkedList


def test_1_instantiate():
    """
    Task 1: The LinkedList should instantiate with an empty head.
    """
    ll = LinkedList()
    assert ll.head is None, "The linked list's head should be None."


def test_2_insert_in_head():
    """
    Task 2: The insert method should insert a new element at the head of the list.
    """
    ll = LinkedList()
    ll.insert(1)
    assert ll.head.data == 1, "The linked list's head should contain the inserted value."


def test_3_insert_multiple():
    """
    Task 3: Inserting multiple elements should update the head to the most recently added element,
            and the previous head should become the next node after the new head.
    """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)

    assert ll.head.data == 2, "The head should contain the most recently inserted value."
    assert ll.head.next.data == 1, "The next node should contain the previously inserted value."


def test_4_insert_existing():
    """
    Task 4: Inserting an existing element should move the existing node to the right,
            and the new node should become the head.
    """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(1)

    assert ll.head.data == 1, "The head should contain the most recently inserted value."
    assert ll.head.next.data == 2, "The next node should contain the next inserted value."
    assert ll.head.next.next.data == 1, "The following node should contain the repeated value."


def test_5_find_existing_element():
    """
    Task 5: The find method should return True if the element exists in the list.
    """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)

    assert ll.find(2) == True, "Find should return True for existing elements."


def test_6_find_non_existing_element():
    """
    Task 6: The find method should return False if the element does not exist in the list.
    """
    ll = LinkedList()
    ll.insert(1)

    assert ll.find(3) == False, "Find should return False for non-existing elements."


def test_7_delete_existing_element():
    """
    Task 7: The delete method should remove an existing element from the list.
    """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.delete(2)

    assert ll.find(2) == False, "Deleted element should not be found."


def test_8_delete_non_existing_element():
    """
    Task 8: Trying to delete a non-existing element should not modify the list.
    """
    ll = LinkedList()
    ll.insert(1)
    ll.delete(2)

    assert ll.find(1) == True, "Existing elements should remain if a non-existing element is deleted."


def test_9_linked_list_length():
    """
    Task 9: The LinkedList should correctly report its length/size.
    """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)

    assert len(ll) == 2, "The length should be correctly reported."


def test_10_linked_list_to_list():
    """
    Task 10: The LinkedList should be correctly converted to a Python list.
    """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)

    assert ll.to_list() == [2, 1], "The LinkedList should be correctly converted to a Python list."

