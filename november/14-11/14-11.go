package main

import (
	"fmt"
	"slices"
	"time"
)

func main() {
	fmt.Println("ok")
	//Tests:
	daysUntilWeekend("2025-11-14") //should return "1 day until the weekend.".
	daysUntilWeekend("2025-01-01") //should return "3 days until the weekend.".
	daysUntilWeekend("2025-12-06") //should return "It's the weekend!".
	daysUntilWeekend("2026-01-27") //should return "4 days until the weekend.".
	daysUntilWeekend("2026-09-07") //should return "5 days until the weekend.".
	daysUntilWeekend("2026-11-29") //should return "It's the weekend!".
}

func daysUntilWeekend(dateString string) string {

	t, err := time.Parse("2006-01-02", dateString)

	if err != nil {
		fmt.Println("Fecha inválida")
	}
	day := int(t.Weekday())

	WEEKEND := []int{0, 6}

	message := ""

	if slices.Contains(WEEKEND, day) {
		message = "It's the weekend!"
	} else {
		daysToWeekend := 6 - day

		if daysToWeekend == 1 {
			message = fmt.Sprintf("%d day until the weekend.", daysToWeekend)
		} else {
			message = fmt.Sprintf("%d days until the weekend.", daysToWeekend)
		}
	}

	fmt.Println(message)

	return message
}
