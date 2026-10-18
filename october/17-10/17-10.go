package main

import "fmt"

func main() {

	fmt.Println("hello from golang")

	mask("4012-8888-8888-1881") //should return "****-****-****-1881".
	mask("5105 1051 0510 5100") //should return "**** **** **** 5100".
	mask("6011 1111 1111 1117") //should return "**** **** **** 1117".
	mask("2223-0000-4845-0010") //should return "****-****-****-0010".

}

func mask(card string) string {

	var maskedVersion string = ""

	for i := 0; i < len(card); i++ {

		if i < len(card)-4 {
			if string(card[i]) == " " || string(card[i]) == "-" {

				maskedVersion += string(card[i])

			} else {

				maskedVersion += "*"

			}
		} else {

			maskedVersion += string(card[i])

		}

	}

	fmt.Println(maskedVersion)

	return maskedVersion
}
