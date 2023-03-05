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
 * @return bool布尔型
 */
func hasCycle(head *ListNode) bool {
	// write code here

	var p, q *ListNode
	p = head
	q = p

	for q != nil && q.Next != nil {
		p = p.Next
		q = q.Next

		if q == nil {
			return false
		}

		q = q.Next

		if p == q {
			return true
		}
	}

	return false
}
