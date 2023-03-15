package core

import (
	"math/rand"
	"time"
)

func RandUser(n, m int) int {
	// 随机获取 n,m 范围内的用户id
	rand.Seed(time.Now().UnixNano())
	r := rand.Intn(m-n) + n
	return r
}
