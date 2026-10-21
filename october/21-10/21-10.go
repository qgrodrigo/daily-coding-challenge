package main

import "fmt"

func main() {

	fmt.Println("hello")
	//Tests
	adjustThermostat(32, 0)    //should return "Hold".
	adjustThermostat(70, 25)   //should return "Heat: 7.0 degrees Fahrenheit".
	adjustThermostat(72, 18)   //should return "Cool: 7.6 degrees Fahrenheit".
	adjustThermostat(212, 100) //should return "Hold".
	adjustThermostat(59, 22)   //should return "Heat: 12.6 degrees Fahrenheit".
}

func adjustThermostat(currentF float64, targetC float64) string {

	var targetCToF float64 = (targetC * 1.8) + 32
	var message string

	if currentF == targetCToF {
		message = "Hold"
		fmt.Println(message)
	}
	if currentF < targetCToF {
		message = fmt.Sprintf("Heat: %.1f degrees Fahrenheit", targetCToF-currentF)
		fmt.Println(message)

	}

	if currentF > targetCToF {
		message = fmt.Sprintf("Heat: %.1f degrees Fahrenheit", currentF-targetCToF)
		fmt.Println(message)
	}

	return message

}
