package main

import (
	"fmt"
	"strconv"
)

func main() {

	fmt.Println("online")

	//Tests
	format(500)   //should return "8:20".
	format(4000)  //should return "1:06:40".
	format(1)     //should return "0:01".
	format(5555)  //should return "1:32:35".
	format(99999) //should return "27:46:39".

}

func format(seconds int) string {

	var hoursText string = ""
	var minutesText string = ""
	var secondsText string = ""
	var formatedTime string = ""

	var hours int = seconds / 3600
	var minutes int = (seconds % 3600) / 60
	var restSeconds int = (seconds % 3600) % 60

	if restSeconds < 10 {
		secondsText = "0" + strconv.Itoa(seconds)
	} else {
		secondsText = strconv.Itoa(restSeconds)
	}

	if minutes < 0 {
		minutesText = "0"
	} else if minutes > 0 && minutes < 10 {
		if hours < 1 {
			minutesText = strconv.Itoa(minutes)
		} else {
			minutesText = "0" + strconv.Itoa(minutes)
		}
	} else {
		minutesText = strconv.Itoa(minutes)
	}

	if hours > 0 {
		hoursText = strconv.Itoa(hours) + ":"
	}

	formatedTime = hoursText + minutesText + ":" + secondsText
	fmt.Println(formatedTime)

	return formatedTime
}
