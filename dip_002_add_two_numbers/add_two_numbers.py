class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers:
    @staticmethod
    def add_two_numbers(l1, l2, c=0):
        result = 0

        # Iterates each list from left to right at the same time
        while l1 is not None and l2 is not None:
            # Add the values
            sum = c + l1.val + l2.val

            if len(str(sum)) > 1:
                # If sum is greater than 9 establishes value of c
                # and adds only first number
                c = int(str(sum)[0])
                sum = int(str(sum)[1::])

            if result == 0:
                # First result, creates first node
                temp_result = ListNode(sum)
                result = temp_result
            else:
                # Inserts new nodes in previous result
                temp_result.next = ListNode(sum)
                temp_result = temp_result.next

            # Next nodes
            l1 = l1.next
            l2 = l2.next

        return result
