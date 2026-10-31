package main

import "fmt"

func main() {

	fmt.Println("ok")
	//Tests
	nthPrime(5)    //should return 11.
	nthPrime(10)   //should return 29.
	nthPrime(16)   //should return 53.
	nthPrime(99)   //should return 523.
	nthPrime(1000) //should return 7919.
}

func nthPrime(n int) int {

	count := 0
	index := 1
	lastPrime := 0

	for {

		if isPrime(index) == true {
			count += 1
			lastPrime = index
		}

		index += 1

		if count >= n {
			break
		}
	}

	fmt.Println(lastPrime)

	return lastPrime
}

func isPrime(number int) bool {

	isPrime := true

	if number <= 1 {
		isPrime = false
	}

	for i := 2; i < number-1; i++ {
		if number%i == 0 {
			isPrime = false
			break
		} else {
			continue
		}
	}

	return isPrime
}
