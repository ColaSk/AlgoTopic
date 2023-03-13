package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 *
 * @param nums int整型一维数组
 * @param target int整型
 * @return int整型
 */
func search(nums []int, target int) int {
	// write code here
	var start int = 0
	var end int = len(nums) - 1
	var middle int

	if end < 0 {
		return -1
	}

	for start <= end {
		middle = (start + end) / 2
		if nums[middle] == target {
			return middle
		}

		if target < nums[middle] {
			end = middle - 1
		} else {
			start = middle + 1
		}
	}

	return -1
}
