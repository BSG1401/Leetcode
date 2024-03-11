class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res=[]
        temp=head
        while temp is not None:
            l=temp.next
            while l is not None and l.val<=temp.val:
                l=l.next
            if l is None:
                res.append(0)
            else:
                res.append(l.val)
            temp=temp.next
        return res
