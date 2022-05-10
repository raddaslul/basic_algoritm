class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        # head 앞을 prev로 선언하여 None으로 초기화 한 후 node가 head에서 next로 이동하면서 해당 node를 prev에 연결시키는 방식   
        prev = None # prev를 None으로 선언
        node = head

        while node:
            next = node.next
            node.next = prev # node를 prev와 연결

            # 다음 노드로 이동하여 동일한 로직 실행
            prev = node 
            node = next

        return prev
