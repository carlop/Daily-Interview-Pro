class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers:
    @staticmethod
    def add_two_numbers(l1, l2, c=0):
        # Linkded list with the result
        result = 0

        # Iterates each list from left to right at the same time
        while l1 is not None and l2 is not None:
            # Add the values
            valid_sum = c + l1.val + l2.val

            if len(str(valid_sum)) > 1:
                # If sum is greater than 9 establishes value of c
                # and adds only first number
                c = int(str(valid_sum)[0])
                valid_sum = int(str(valid_sum)[1::])

            if result is 0:
                # First result, creates first node
                temp_result = ListNode(valid_sum)
                result = temp_result
            else:
                # Inserts new nodes in previous result
                temp_result.next = ListNode(valid_sum)
                temp_result = temp_result.next

            # Next nodes
            l1 = l1.next
            l2 = l2.next

        return result
