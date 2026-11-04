package main

import (
	"fmt"
	"strings"
)

func main() {
	//fmt.Println("ok")
	//Tests
	imageSearch([]string{"dog.png", "cat.jpg", "parrot.jpeg"}, "dog")                                         //should return ["dog.png"].
	imageSearch([]string{"Sunset.jpg", "Beach.png", "sunflower.jpeg"}, "sun")                                 //should return ["Sunset.jpg", "sunflower.jpeg"].
	imageSearch([]string{"Moon.png", "sun.jpeg", "stars.png"}, "PNG")                                         //should return ["Moon.png", "stars.png"].
	imageSearch([]string{"cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"}, "Cat") //should return ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"].
}

func imageSearch(images []string, term string) []string {

	searchResult := []string{}

	for _, image := range images {
		if strings.Contains(strings.ToLower(image), strings.ToLower(term)) {
			searchResult = append(searchResult, image)
		}
	}
	fmt.Println(searchResult)

	return searchResult
}
