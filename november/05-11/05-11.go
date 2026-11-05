package main

import (
	"fmt"
)

func main() {
	//fmt.Println("hello")
	//Tests
	buildMatrix(2, 3) //should return [[0, 0, 0], [0, 0, 0]].
	buildMatrix(3, 2) //should return [[0, 0], [0, 0], [0, 0]].
	buildMatrix(4, 3) //should return [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]].
	buildMatrix(9, 1) //should return [[0], [0], [0], [0], [0], [0], [0], [0], [0]].
}

func buildMatrix(rows int, cols int) [][]int {

	filledMatrix := [][]int{}

	for i := 0; i < rows; i++ {
		row := make([]int, cols)
		filledMatrix = append(filledMatrix, row)
	}

	fmt.Println(filledMatrix)

	return filledMatrix
}
