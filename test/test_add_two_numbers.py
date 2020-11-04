import unittest

from dip_002_add_two_numbers.add_two_numbers import ListNode, AddTwoNumbers


class AddTwoNumbersTest(unittest.TestCase):

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    def test_708(self):
        result = AddTwoNumbers().add_two_numbers(self.l1, self.l2)
        l_result = ListNode(7)
        l_result.next = ListNode(0)
        l_result.next.next = ListNode(8)
        while result is not None and l_result is not None:
            self.assertEqual(result.val, l_result.val)
            result = result.next
            l_result = l_result.next


if __name__ == '__main__':
    unittest.main()
