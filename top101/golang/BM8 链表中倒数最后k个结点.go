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
 * @param pHead ListNode类
 * @param k int整型
 * @return ListNode类
 */
func FindKthToTail(pHead *ListNode, k int) *ListNode {
	// write code here

	var start *ListNode = pHead
	var end *ListNode = pHead

	if start == nil {
		return nil
	}

	for i := 0; i < k; i++ {
		if end == nil {
			return nil
		}
		end = end.Next
	}

	for end != nil {
		start = start.Next
		end = end.Next
	}

	return start

}
