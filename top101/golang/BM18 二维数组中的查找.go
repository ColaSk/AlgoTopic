package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param target int整型
 * @param array int整型二维数组
 * @return bool布尔型
 */
func Find(target int, array [][]int) bool {
	// write code here

	if len(array) == 0 || len(array[0]) == 0 {
		return false
	}

	rows := len(array)
	cols := len(array[0])

	i := 0
	j := cols - 1

	for i < rows && j >= 0 {
		if target == array[i][j] {
			return true
		} else if target < array[i][j] {
			j--
		} else {
			i++
		}
	}

	return false

}
