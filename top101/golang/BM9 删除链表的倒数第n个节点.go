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
 * @param n int整型
 * @return ListNode类
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// write code here

	var newNode *ListNode = &ListNode{}
	newNode.Next = head

	var start, end *ListNode = head, head
	var pre *ListNode = newNode

	for i := 0; i < n; i++ {
		end = end.Next
	}

	for end != nil {
		pre = start
		start = start.Next
		end = end.Next
	}

	pre.Next = start.Next

	return newNode.Next
}
