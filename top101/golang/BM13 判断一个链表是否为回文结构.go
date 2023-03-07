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
 * @param head ListNode类 the head
 * @return bool布尔型
 */
func isPail(head *ListNode) bool {
	// write code here

	// 创建节点列表
	var list []*ListNode = make([]*ListNode, 0)

	// 加入节点列表
	for p := head; p != nil; {
		list = append(list, p)
		p = p.Next
	}

	i := 0
	j := len(list) - 1

	if j < 0 {
		return false
	}

	for i < j {
		if list[i].Val != list[j].Val {
			return false
		}
		i++
		j--
	}

	return true

}
