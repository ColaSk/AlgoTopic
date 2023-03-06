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
 * @param head1 ListNode类
 * @param head2 ListNode类
 * @return ListNode类
 */
func ReverseList(pHead *ListNode) *ListNode {
	// write code here
	// 反转链表

	var pre *ListNode = pHead
	var temp *ListNode
	var newNode *ListNode = &ListNode{Next: pHead}

	for pre != nil && pre.Next != nil {
		temp = pre.Next
		pre.Next = temp.Next
		temp.Next = newNode.Next
		newNode.Next = temp
	}

	return newNode.Next

}

func addInList(head1 *ListNode, head2 *ListNode) *ListNode {
	// write code here
	carry := 0     // 进位
	remainder := 0 // 余数
	// quotient := 0 // 商数
	augend := 0 // 被加数
	addend := 0 //加数

	var result *ListNode = &ListNode{} // 结果指针
	var resultPre *ListNode = result

	p1 := ReverseList(head1)
	p2 := ReverseList(head2)

	for p1 != nil || p2 != nil {

		if p1 != nil {
			augend = p1.Val
			p1 = p1.Next
		} else {
			augend = 0
		}

		if p2 != nil {
			addend = p2.Val
			p2 = p2.Next
		} else {
			addend = 0
		}

		r := augend + addend + carry
		remainder = r % 10
		carry = r / 10

		resultPre.Next = &ListNode{Val: remainder}
		resultPre = resultPre.Next

	}

	if carry != 0 {
		resultPre.Next = &ListNode{Val: carry}
	}

	result = ReverseList(result.Next)

	return result
}
