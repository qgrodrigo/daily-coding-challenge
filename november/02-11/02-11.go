package main

import (
	"fmt"
	"math"
)

func main() {
	//fmt.Println("hello")

	// Tests:
	infected(1)  //should return 2.
	infected(3)  //should return 6.
	infected(8)  //should return 152.
	infected(17) //should return 39808.
	infected(25) //should return 5217638.
}

func infected(days int) int {
	infectedCount := 1

	for i := 1; i < days+1; i++ {
		infectedCount *= 2

		if i%3 == 0 {
			parchCount := math.Ceil(float64(infectedCount) * 0.2)
			infectedCount -= int(parchCount)
		}
	}

	fmt.Println(infectedCount)

	return infectedCount
}
