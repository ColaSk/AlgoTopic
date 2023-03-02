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
 * @param m int整型
 * @param n int整型
 * @return ListNode类
 */
func reverseBetween(head *ListNode, m int, n int) *ListNode {
	// write code here

	var pre *ListNode // 待反转节点的头节点
	var curr *ListNode
	var temp *ListNode
	var newNode *ListNode = &ListNode{}

	newNode.Next = head // 定义一个头节点，使他的下一个节点为输入节点
	curr = newNode.Next // 当前节点
	pre = newNode       // 指定待转节点的头节点

	for i := 1; i < n; i++ {
		// 找到待转节点与他的头节点
		if i < m {
			pre = curr
			curr = pre.Next
			// 节点转换
		} else {
			temp = curr.Next
			curr.Next = temp.Next
			temp.Next = pre.Next
			pre.Next = temp
		}
	}

	return newNode.Next

}
