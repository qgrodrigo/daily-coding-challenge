package main

import (
	"fmt"
	"unicode"
)

func main() {
	// Tests:
	verify("foo", "bar", 57)                                                //should return True.
	verify("foo", "bar", 54)                                                //should return False.
	verify("freeCodeCamp", "Rocks", 238)                                    //should return True.
	verify("Is this valid?", "No", 210)                                     //should return False.
	verify("Is this valid?", "Yes", 233)                                    //should return True.
	verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) //should return True.
}

func verify(message string, key string, signature int) bool {

	messageSum := 0
	keySum := 0
	isMatched := true

	for _, char := range message {
		messageSum += letterValue(string(char))
	}

	for _, char := range key {
		keySum += letterValue(string(char))
	}

	if messageSum+keySum != signature {
		isMatched = false
	}

	fmt.Println(isMatched)

	return isMatched
}

func letterValue(letter string) int {
	value := 0

	if unicode.IsLower(rune(letter[0])) {
		value = int(rune(letter[0])) - 96
	}

	if unicode.IsUpper(rune(letter[0])) {
		value = int(rune(letter[0])) - 38
	}

	return value
}
