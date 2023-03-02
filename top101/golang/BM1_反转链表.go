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
 * @param pHead ListNode类
 * @return ListNode类
 */
func ReverseList(pHead *ListNode) *ListNode {
	// write code here
	var curr *ListNode = pHead
	var pre *ListNode
	var temp *ListNode

	for curr != nil {
		temp = curr.Next
		curr.Next = pre
		pre = curr
		curr = temp
	}

	return pre
}
