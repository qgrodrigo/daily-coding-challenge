package main

import (
	"fmt"
	"strings"
)

func main() {
	//fmt.Println("hi!")
	//Tests:
	getExtension("document.txt")   //should return "txt".
	getExtension("README")         //should return "none".
	getExtension("image.PNG")      //should return "PNG".
	getExtension(".gitignore")     //should return "gitignore".
	getExtension("archive.tar.gz") //should return "gz".
	getExtension("final.draft.")   //should return "none".
}

func getExtension(filename string) string {

	fileParts := strings.Split(filename, ".")
	extension := "none"

	if strings.Contains(filename, ".") {
		extension = fileParts[len(fileParts)-1]
	}

	if extension == "" {
		extension = "none"
	}

	fmt.Println(extension)

	return extension
}
