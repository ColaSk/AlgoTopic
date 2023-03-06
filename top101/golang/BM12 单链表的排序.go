package main

import (
	. "nc_tools"
	"sort"
)

/*
 * type ListNode struct{
 *   Val int
 *   Next *ListNode
 * }
 */

/**
 *
 * @param head ListNode类 the head node
 * @return ListNode类
 */
func sortInList(head *ListNode) *ListNode {
	// write code here

	// 创建节点列表
	var list []*ListNode = make([]*ListNode, 0)
	var newNode *ListNode = &ListNode{}
	var pp *ListNode = newNode

	// 加入节点列表
	for p := head; p != nil; {
		list = append(list, p)
		p = p.Next
	}

	// 对list进行排序
	sort.Slice(list, func(i, j int) bool { return list[i].Val < list[j].Val })

	// 重新编排
	for _, node := range list {
		pp.Next = node
		pp = pp.Next
	}

	pp.Next = nil

	return newNode.Next

}
