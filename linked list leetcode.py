# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1, num2 = "", ""
        def linked_to_str(arr,string):
            if arr.next==None: return string + str(arr.val)
            return linked_to_str(arr.next,string) + str(arr.val)
        num1 = linked_to_str(l1,"")
        num2 = linked_to_str(l2,"")
        num3 = str(int(num1) + int(num2))[::-1]

        def str_to_linked(s):
            if not s:
                return None
            head = ListNode(s[0])
            current = head
            for char in s[1:]:
                current.next = ListNode(char)
                current = current.next
            return head


        return str_to_linked(num3)












sol = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol.addTwoNumbers(l1, l2)



