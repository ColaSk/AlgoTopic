package core

import (
	"math/rand"
	"sort"
)

/*根据权重随机生成器

* 原理: 假设我有一组数字：{1,2,3,4}, 他们的权重分别为{1, 1/2,1/3,1/4},比例为12:6:4:3, 一般方案的随机应该为从
* {1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4} （数组将被打乱）中随机生成一个下标取值，这样的问题是
* 会占用大量无用空间，因此我们计算权重总和sum，然后再1与sum中间随机选取一个数R，通过统计遍历项之和，大于R就停止遍历，
* 取此处的项
* 在程序中进行了部分优化：1）提前计算好当前项与之前所有项之和 2）通过二分查找的方式进行查找

 */

// 定义元素对象
type Choice struct {
	Item   interface{}
	Weight float64
}

// 定义选择器
type WeightedChooser struct {
	data   []Choice
	totals []float64
	max    float64
}

func (ch *WeightedChooser) Rand() interface{} {
	// 获取随机

	r := rand.Float64() * ch.max
	i := sort.SearchFloat64s(ch.totals, r)

	return ch.data[i].Item
}

func NewChooser(ce ...Choice) WeightedChooser {

	// 权重元素升序排序
	sort.Slice(ce, func(i, j int) bool {
		return ce[i].Weight < ce[j].Weight
	})

	totals := make([]float64, len(ce))
	total := 0.0

	for i, c := range ce {
		total += c.Weight
		totals[i] = total
	}

	return WeightedChooser{data: ce, totals: totals, max: total}
}
