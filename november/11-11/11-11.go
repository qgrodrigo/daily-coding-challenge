package main

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	//fmt.Println("ok")
	//Tests:
	count("Hello World")                                  //should return [3, 7].
	count("JavaScript")                                   //should return [3, 7].
	count("Python")                                       //should return [1, 5].
	count("freeCodeCamp")                                 //should return [5, 7].
	count("Hello, World!")                                //should return [3, 7].
	count("The quick brown fox jumps over the lazy dog.") //should return [11, 24].
}

func count(str string) []string {

	str = strings.ToLower(str)
	vowels := []string{"a", "e", "i", "o", "u"}
	vowelsCount := 0
	consonantsCount := 0

	for _, char := range str {
		if unicode.IsLetter(char) {
			if slices.Contains(vowels, string(char)) {
				vowelsCount += 1
			} else {
				consonantsCount += 1
			}
		}
	}

	fmt.Println([]string{strconv.Itoa(vowelsCount), strconv.Itoa(consonantsCount)})

	return []string{strconv.Itoa(vowelsCount), strconv.Itoa(consonantsCount)}
}
