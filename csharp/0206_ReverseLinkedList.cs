// 206. Reverse Linked List (Easy)
// https://leetcode.com/problems/reverse-linked-list/
//
// Approach: iterative pointer reversal. Walk the list once, flipping each
// node's next pointer to the previous node. O(n) time, O(1) space.

public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public ListNode ReverseList(ListNode head)
    {
        ListNode prev = null;
        ListNode current = head;
        while (current != null)
        {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
}
