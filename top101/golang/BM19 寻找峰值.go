package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 *
 * @param nums int整型一维数组
 * @return int整型
 */
func findPeakElement(nums []int) int {
	// write code here

	start := 0
	end := len(nums) - 1

	if end == 0 {
		return 0
	}

	for start < end {
		middle := (start + end) / 2

		if nums[middle] > nums[middle+1] {
			end = middle // 向下趋势
		} else {
			start = middle + 1 // 向上趋势
		}

	}

	return start
}
