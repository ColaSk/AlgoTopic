package main

/**
 *
 * @param rotateArray int整型一维数组
 * @return int整型
 */
func minNumberInRotateArray(rotateArray []int) int {
	// write code here

	k := 0
	lens := len(rotateArray)

	if lens == 1 {
		return rotateArray[k]
	}

	for i := 1; i < lens; i++ {
		if rotateArray[i-1] > rotateArray[i] {
			k = i
			break
		}
	}

	return rotateArray[k]

}
