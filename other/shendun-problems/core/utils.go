package core

import (
	"math/rand"
	"os"
	"time"
)

func RandWeight(n, m int) int {
	// 随机生成 n,m 范围内的重量
	rand.Seed(time.Now().UnixNano())
	r := rand.Intn(m-n) + n
	return r
}

func Exist(path string) bool {
	// 判断文件是否存在
	_, err := os.Lstat(path)
	return !os.IsNotExist(err)
}
