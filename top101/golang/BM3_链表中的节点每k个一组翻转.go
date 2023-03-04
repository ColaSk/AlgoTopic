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
 * @param k int整型
 * @return ListNode类
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
	// write code here
	var start *ListNode
	var end *ListNode
	var pre *ListNode
	var temp *ListNode
	var newNode *ListNode = &ListNode{}

	var m int = 1
	var n int = k
	var i int = 1
	var j int = 1

	newNode.Next = head
	pre = newNode
	start = newNode.Next
	end = start

	for start != nil && end != nil {

		// 获取分组的终点
		for ; j < n && end != nil; j++ {
			end = end.Next
		}

		if end == nil {
			return newNode.Next
		}

		// 获取分组后进行反转
		for ; i < n; i++ {
			if i < m {
				pre = start
				start = start.Next
			} else {
				temp = start.Next
				start.Next = temp.Next
				temp.Next = pre.Next
				pre.Next = temp
			}
		}

		m = n + 1
		n = m + k - 1
		i = m
		j = i
		pre = start
		start = pre.Next
		end = start

	}

	return newNode.Next
}
