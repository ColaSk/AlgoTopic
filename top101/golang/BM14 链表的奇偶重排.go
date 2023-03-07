package main

import . "nc_tools"

/*
 * type ListNode struct{
 *   Val int
 *   Next *ListNode
 * }
 */

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 *
 * @param head ListNode类
 * @return ListNode类
 */
func oddEvenList(head *ListNode) *ListNode {
	// write code here

	if head == nil || head.Next == nil {
		return head
	}

	var p *ListNode = head
	var q *ListNode = p.Next
	var qHead *ListNode = q

	for q != nil && q.Next != nil {

		p.Next = q.Next
		p = p.Next
		q.Next = p.Next
		q = q.Next
	}

	p.Next = qHead

	return head

}
