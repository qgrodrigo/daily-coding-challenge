package main

import (
	"fmt"
	"time"
)

func main() {
	//fmt.Println("ok")
	//Tests
	getWeekday("2025-11-06") //should return Thursday.
	getWeekday("1999-12-31") //should return Friday.
	getWeekday("1111-11-11") //should return Saturday.
	getWeekday("2112-12-21") //should return Wednesday.
	getWeekday("2345-10-01") //should return Monday.
}

func getWeekday(dateString string) string {

	t, err := time.Parse("2006-01-02", dateString)

	if err != nil {
		fmt.Println("Fecha inválida")
	}

	dayOfWeek := t.Weekday().String()

	fmt.Println(dayOfWeek)

	return dayOfWeek
}
