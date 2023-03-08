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

	var p *ListNode = head

	if p == nil || p.Next == nil {
		return head
	}

	for p.Next != nil {
		if p.Val == p.Next.Val {
			p.Next = p.Next.Next
		} else {
			p = p.Next
		}
	}

	return head
}
