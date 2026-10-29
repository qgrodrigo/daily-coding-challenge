package main

import (
	"fmt"
	"strings"
)

func main() {
	//Tests:
	navigate([]string{"Visit About Us", "Back", "Forward"})                                       //should return "About Us".
	navigate([]string{"Forward"})                                                                 //should return "Home".
	navigate([]string{"Back"})                                                                    //should return "Home".
	navigate([]string{"Visit About Us", "Visit Gallery"})                                         //should return "Gallery".
	navigate([]string{"Visit About Us", "Visit Gallery", "Back", "Back"})                         //should return "Home".
	navigate([]string{"Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"})        //should return "Contact".
	navigate([]string{"Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"}) //should return "Visit Us".
}

func navigate(commands []string) string {
	back := []string{}
	current := "Home"
	forward := []string{}

	for _, command := range commands {
		if strings.HasPrefix(command, "Visit") {
			page := command[6:]
			back = append(back, current)
			current = page
			forward = []string{}
		}

		if command == "Back" {
			if len(back) > 0 {
				forward = append(forward, current)
				current = back[len(back)-1]
				back = back[:len(back)-1]
			}
		}

		if command == "Forward" {
			if len(forward) > 0 {
				back = append(back, current)
				current = forward[0]
			}
		}
	}

	fmt.Println(current)
	return current
}
