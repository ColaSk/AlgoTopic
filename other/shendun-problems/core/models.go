package core

import (
	"strconv"

	"gorm.io/gorm"
)

// 订单表
type Order struct {
	gorm.Model
	Uid    int64   `gorm:"index"` // 用户id
	Weight float64 // 重量 (单位KG)
}

func (o *Order) Format() string {
	id := strconv.FormatInt(int64(o.ID), 10)
	uid := strconv.FormatInt(o.Uid, 10)
	weight := strconv.FormatFloat(o.Weight, 'f', 2, 64)
	created := o.CreatedAt.Format("2006-01-02 15:04:05")
	return "ID: " + string(id) + " Uid: " + uid + " Weight: " + weight + " CreatedAt: " + created
}
