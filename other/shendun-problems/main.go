package main

import (
	"freight/core"
	"os"

	"fmt"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var NUM = 100000    // 订单数量
var PAGE_SIZE = 100 // 订单一页几个
var SQLITE_PATH = "test.db"

func GetWeightedChooserForWeight(n, m int) core.WeightedChooser {
	// 获取关于重量的权重生成器

	// 生成权重
	var weights []core.Choice
	for i := 1; i <= m-n; i++ {
		weights = append(weights, core.Choice{Item: float64(i), Weight: 1.0 / float64(i)})
	}

	return core.NewChooser(weights...)

}

var CHOOSER = GetWeightedChooserForWeight(1, 100)

func RandCreateOrders(num int) []core.Order {
	// 随机生成num个订单数据

	var orders []core.Order

	for i := 0; i < num; i++ {
		uid := core.RandUser(1, 1000)
		weight := CHOOSER.Rand().(float64)

		orders = append(orders, core.Order{Uid: int64(uid), Weight: weight})
	}

	return orders
}

func CreatePages(nums, size int) int {
	// 获取最大页数

	page := nums / size
	rem := nums % size

	if rem != 0 {
		page++
	}

	return page
}

func main() {

	// 存在要删除
	if core.Exist(SQLITE_PATH) {
		err := os.Remove(SQLITE_PATH)

		if err != nil {
			fmt.Println("删除文件: "+SQLITE_PATH+"ERROR: ", err)
			return
		}
	}

	db, err := gorm.Open(sqlite.Open(SQLITE_PATH), &gorm.Config{})

	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&core.Order{}) // 初始化订单表

	pages := CreatePages(NUM, PAGE_SIZE)

	for i := 1; i <= pages; i++ {

		size := PAGE_SIZE

		// 取到最后一页的数据量
		if i == pages {
			rem := NUM % PAGE_SIZE
			if rem != 0 {
				size = rem
			}
		}

		fmt.Println("开始创建订单: ", i*size)
		orders := RandCreateOrders(size)
		db.Create(&orders)
		fmt.Println("创建订单结束: ", i*size)
	}

	var uid int64

	for {
		fmt.Print("请输入用户ID:")
		fmt.Scanln(&uid)

		if uid <= 0 {
			fmt.Println("输入的ID: ", uid, "不合法, exit ...")
			break
		}
		fmt.Println("开始查询用户: ", uid, "的全部订单...")

		var orders []core.Order
		var costs float64 = 0

		db.Where("Uid = ?", uid).Find(&orders)

		fmt.Println("用户: ", uid, "的全部订单如下: ")
		fmt.Println("============================")
		for _, order := range orders {
			fmt.Println(order.Format())
			cost := core.CalculateFreight(order.Weight)
			costs += cost
			fmt.Println("用户: ", uid, " 订单: ", order.ID, " 费用: ", cost)
			fmt.Println("------------------------------")
		}
		fmt.Println("用户: ", uid, " 总费用: ", costs)
		fmt.Println("============================")
	}

}
