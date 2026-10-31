package main

import (
	"fmt"
	"strings"
)

func main() {

	//Tests
	spookify("hello_world")                         //should return "HeLlO~wOrLd".
	spookify("Spooky_Case")                         //should return "SpOoKy~CaSe".
	spookify("TRICK-or-TREAT")                      //should return "TrIcK~oR~tReAt".
	spookify("c_a-n_d-y_-b-o_w_l")                  //should return "C~a~N~d~Y~~b~O~w~L".
	spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") //should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".
}

func spookify(boo string) string {

	boo = strings.ReplaceAll(boo, "-", "~")
	boo = strings.ReplaceAll(boo, "_", "~")
	spookyBoo := ""
	count := 0

	for _, char := range boo {
		if string(char) != "~" {
			if count%2 == 0 {
				spookyBoo += strings.ToUpper(string(char))
			} else {
				spookyBoo += strings.ToLower(string(char))
			}
			count += 1
		} else {
			spookyBoo += string(char)
		}
	}

	fmt.Println(spookyBoo)
	return spookyBoo
}
