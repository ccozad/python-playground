import reverse_linked_list

def test_append_node():
    linked_list = reverse_linked_list.LinkedList()
    linked_list.append_node('A')
    linked_list.append_node('B')
    linked_list.append_node('C')
    expected_outcome = 'A -> B -> C'

    assert str(linked_list) == expected_outcome

def test_reverse():
    linked_list = reverse_linked_list.LinkedList()
    linked_list.append_node('A')
    linked_list.append_node('B')
    linked_list.append_node('C')
    linked_list.append_node('D')
    linked_list.append_node('E')
    linked_list.append_node('F')
    original_order = str(linked_list)
    expected_outcome1 = 'A -> B -> C -> D -> E -> F'
    linked_list.reverse()
    reverse_order = str(linked_list)
    expected_outcome2 = 'F -> E -> D -> C -> B -> A'

    assert original_order == expected_outcome1
    assert reverse_order == expected_outcome2