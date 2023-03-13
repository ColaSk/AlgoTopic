package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param data int整型一维数组
 * @return int整型
 */

func InversePairs(data []int) int {
	// write code here
	pre := 0
	length := len(data)
	result := make([]int, length)

	if length == 0 || length == 1 {
		return 0
	}

	for interval := 1; interval < length; interval = 2 * interval {

		for start := 0; start < length; start += 2 * interval {

			end := start + 2*interval
			mid := start + interval
			low := start

			if end > length {
				end = length
			}

			if mid > length {
				mid = length
			}

			s1, e1 := start, mid
			s2, e2 := mid, end

			for s1 < e1 && s2 < e2 {
				if data[s1] > data[s2] {
					result[low] = data[s2]
					s2++
					low++
					pre += mid - s1
				} else {
					result[low] = data[s1]
					s1++
					low++
				}
			}

			for s1 < e1 {
				result[low] = data[s1]
				s1++
				low++
			}

			for s2 < e2 {
				result[low] = data[s2]
				s2++
				low++
			}

		}
		data, result = result, data
	}
	return pre % 1000000007
}
