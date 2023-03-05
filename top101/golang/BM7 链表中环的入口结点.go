package main

import (
	"fmt"
	. "nc_tools"
)

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

func EntryNodeOfLoop(pHead *ListNode) *ListNode {

	var p, q *ListNode
	p = pHead
	q = p

	// 判断有环
	for q != nil {
		p = p.Next
		q = q.Next

		if q == nil || q.Next == nil {
			return nil
		}

		q = q.Next

		if p == q {
			break
		}
	}

	fmt.Println(p.Val, q.Val)

	if q == nil {
		return nil
	}

	// 查找入口点
	q = pHead

	for p != q {

		p = p.Next
		q = q.Next
	}

	return p

}
