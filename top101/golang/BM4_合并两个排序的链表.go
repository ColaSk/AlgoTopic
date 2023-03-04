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
 * @param pHead1 ListNode类
 * @param pHead2 ListNode类
 * @return ListNode类
 */
func Merge(pHead1 *ListNode, pHead2 *ListNode) *ListNode {
	// write code here
	var newNode *ListNode = &ListNode{}
	var p *ListNode = newNode
	var p1 *ListNode = pHead1
	var p2 *ListNode = pHead2

	for p1 != nil && p2 != nil {
		if p1.Val < p2.Val {
			p.Next = p1
			p = p.Next
			p1 = p1.Next
		} else {
			p.Next = p2
			p = p.Next
			p2 = p2.Next
		}
	}

	if p1 == nil {
		p.Next = p2
	} else {
		p.Next = p1
	}

	return newNode.Next
}
