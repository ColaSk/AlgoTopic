package core

import (
	"math"
)

var FIRST_WEIGHT float64 = 18    // 首重
var MAX_WEIGHT float64 = 100     // 最大重量
var EXTRA_FREIGHT float64 = 5    // 附加费用
var PREMIUM_RATIO float64 = 0.01 //保费比例

func Ceil2Int(num float64) int {
	// float 向上取整转int
	return int(math.Ceil(num))
}

func Round(val float64, precision int) float64 {
	// 四舍五入
	p := math.Pow10(precision)
	return math.Floor(val*p+0.5) / p
}

func CalculateFreight(weight float64) float64 {
	/*  计算运费
	weight: 快递重量， 单位 KG
	*/

	weightInt := Ceil2Int(weight)
	var freight float64 = 0 // 费用

	if weightInt > int(MAX_WEIGHT) {
		weightInt = int(MAX_WEIGHT)
	}

	if weight > 0 && weight <= 1 {
		freight = FIRST_WEIGHT
	} else {
		freight = FIRST_WEIGHT
		overWeight := weightInt - 1 // 超过首重的重量

		for i := 0; i < overWeight; i++ {
			premium := freight * PREMIUM_RATIO          // 保险费用
			freight = freight + premium + EXTRA_FREIGHT // 当前费用

		}
		freight = Round(freight, 0) // 费用四舍五入取整
	}

	return freight
}
