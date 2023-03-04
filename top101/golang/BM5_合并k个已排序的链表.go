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
 * @param lists ListNode类一维数组
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

func mergeKLists(lists []*ListNode) *ListNode {
	// write code here

	var newNode *ListNode
	// 挨个链接，有更优的方案：递归分治
	for _, l := range lists {
		newNode = Merge(newNode, l)
	}

	return newNode

}
