// Exercise 4: Functions
// Create a program that converts temperatures between Celsius and Fahrenheit using functions.
// 1. Write a function toFahrenheit(celsius float64) float64 to convert Celsius to
// Fahrenheit.
// 2. Write a function toCelsius(fahrenheit float64) float64 to convert Fahrenheit
// to Celsius.
// 3. Use these functions to convert temperatures provided as input by the user.

package main

import "fmt"

func toFahrenheit(celsius float64) float64 {
	return (celsius * 9 / 5) + 32
}
func toCelsius(fahrenheit float64) float64 {
	return (fahrenheit - 32) * 5 / 9
}
func main() {
	var temp float64
	var choice int
	fmt.Println("Choose conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
	fmt.Scanf("%d", &choice)
	fmt.Print("Enter temperature: ")
	fmt.Scanf("%f", &temp)
	if choice == 1 {
		fmt.Printf("%.2f°C is %.2f°F\n", temp, toFahrenheit(temp))
	} else if choice == 2 {
		fmt.Printf("%.2f°F is %.2f°C\n", temp, toCelsius(temp))
	} else {
		fmt.Println("Invalid choice!")
	}
}
