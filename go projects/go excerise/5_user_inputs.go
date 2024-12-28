// Exercise 5: Reading User Inputs
// Write a program that asks the user for their name, age, and favorite number.
// 1. Read the inputs and store them in appropriate variables.
// 2. Print a greeting message, including their name, age, and favorite number.

package main

import "fmt"

func main() {
	var name string
	var age int
	var favNumber int
	fmt.Print("Enter your name: ")
	fmt.Scanln(&name)
	fmt.Print("Enter your age: ")
	fmt.Scanf("%d", &age)
	fmt.Print("Enter your favorite number: ")
	fmt.Scanf("%d", &favNumber)
	fmt.Printf("Hello %s! You are %d years old and your favorite number is %d.\n", name, age, favNumber)
}
