package main

import . "nc_tools"

/*
 * type ListNode struct{
 *   Val int
 *   Next *ListNode
 * }
 */

/**
 *
 * @param head ListNode类
 * @return ListNode类
 */
func deleteDuplicates(head *ListNode) *ListNode {
	// write code here

	if head == nil || head.Next == nil {
		return head
	}

	var p *ListNode = head
	var q *ListNode
	var newNode *ListNode = &ListNode{}
	var node *ListNode = newNode

	for p != nil {
		if p.Next == nil || p.Val != p.Next.Val {
			node.Next = p
			p = p.Next
			node = node.Next
			node.Next = nil
		} else {
			q = p.Next
			for q != nil && q.Val == p.Val {
				q = q.Next
			}
			p = q
		}
	}

	return newNode.Next

}
