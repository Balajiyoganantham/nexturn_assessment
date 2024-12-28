// Exercise 1: Data Types and Variables
// You are building a simple application to track daily expenses. Create a program that:
// 1. Declares variables for the following:
// o date (string) to store the date.
// o description (string) to store the description of the expense.
// o amount (float64) to store the expense amount.
// 2. Assign values to the variables and print them in a formatted string.

package main

import "fmt"

func main() {
	var date string = "2024-12-17"
	var description string = "Groceries"
	var amount float64 = 150.75
	fmt.Printf("Date: %s\nDescription: %s\nAmount: $%.2f\n", date, description, amount)
}
