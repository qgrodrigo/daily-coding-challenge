package main

import "fmt"

func main() {
	//fmt.Println("hi!")
	//Tests
	canPost("Hello world")                                                                                  //should return "short post".
	canPost("This is a longer message but still under eighty characters.")                                  //should return "long post".
	canPost("This message is too long to fit into either of the character limits for a social media post.") //should return "invalid post".
}

func canPost(message string) string {

	postType := ""

	if len(message) <= 40 {
		postType = "short post"
	}

	if len(message) > 40 && len(message) <= 80 {
		postType = "long post"
	}

	if len(message) > 80 {
		postType = "invalid post"
	}

	fmt.Println(postType)

	return postType
}
