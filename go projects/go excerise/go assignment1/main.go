package main

import (
	"fmt"
	"math/rand"
)

func trackExpenses() {
	var date, description string
	var amount float64

	date = "2024-12-17"
	description = "Groceries"
	amount = 150.75

	fmt.Printf("Date: %s\nDescription: %s\nAmount: $%.2f\n", date, description, amount)
}

func checkTriangleType() {
	var a, b, c int
	fmt.Println("Enter the sides of the triangle:")
	fmt.Scanf("%d %d %d", &a, &b, &c)

	switch {
	case a == b && b == c:
		fmt.Println("The triangle is Equilateral.")
	case a == b || b == c || a == c:
		fmt.Println("The triangle is Isosceles.")
	default:
		fmt.Println("The triangle is Scalene.")
	}
}

func calculateFactorial() {
	var num int
	fmt.Print("Enter a number: ")
	fmt.Scanf("%d", &num)

	factorial := 1
	for i := 1; i <= num; i++ {
		factorial *= i
	}

	fmt.Printf("Factorial of %d is %d\n", num, factorial)
}

func toFahrenheit(celsius float64) float64 {
	return (celsius * 9 / 5) + 32
}

func toCelsius(fahrenheit float64) float64 {
	return (fahrenheit - 32) * 5 / 9
}

func convertTemperature() {
	var temp float64
	var choice int

	fmt.Println("Choose conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
	fmt.Scanf("%d", &choice)

	fmt.Print("Enter temperature: ")
	fmt.Scanf("%f", &temp)

	switch choice {
	case 1:
		fmt.Printf("%.2f°C is %.2f°F\n", temp, toFahrenheit(temp))
	case 2:
		fmt.Printf("%.2f°F is %.2f°C\n", temp, toCelsius(temp))
	default:
		fmt.Println("Invalid choice!")
	}
}

func readUserInputs() {
	var name string
	var age, favNumber int

	fmt.Print("Enter your name: ")
	fmt.Scanln(&name)

	fmt.Print("Enter your age: ")
	fmt.Scanf("%d", &age)

	fmt.Print("Enter your favorite number: ")
	fmt.Scanf("%d", &favNumber)

	fmt.Printf("Hello %s! You are %d years old and your favorite number is %d.\n", name, age, favNumber)
}
func numberGuessingGame() {

	rand.Seed(42)
	target := rand.Intn(100) + 1
	var guess int
	const maxAttempts = 5

	fmt.Println("Welcome to the Number Guessing Game!")
	fmt.Println("Guess a number between 1 and 100.")

	for attempts := 1; attempts <= maxAttempts; attempts++ {
		fmt.Printf("Attempt %d - Enter your guess: ", attempts)
		fmt.Scan(&guess)

		switch {
		case guess < target:
			fmt.Println("Too low!")
		case guess > target:
			fmt.Println("Too high!")
		default:
			fmt.Printf("Correct! You guessed the number in %d attempts.\n", attempts)
			return
		}
	}

	fmt.Printf("Sorry! You've used all %d attempts. The correct number was %d.\n", maxAttempts, target)
}

func main() {
	for {
		fmt.Println("\nChoose an exercise to run:")
		fmt.Println("1. Track Expenses")
		fmt.Println("2. Check Triangle Type")
		fmt.Println("3. Calculate Factorial")
		fmt.Println("4. Convert Temperature")
		fmt.Println("5. Read User Inputs")
		fmt.Println("6. Number Guessing Game")
		fmt.Println("0. Exit")

		var choice int
		fmt.Print("Enter your choice: ")
		fmt.Scanf("%d", &choice)

		switch choice {
		case 1:
			trackExpenses()
		case 2:
			checkTriangleType()
		case 3:
			calculateFactorial()
		case 4:
			convertTemperature()
		case 5:
			readUserInputs()
		case 6:
			numberGuessingGame()
		case 0:
			fmt.Println("Exiting... Goodbye!")
			return
		default:
			fmt.Println("Invalid choice! Try again.")
		}
	}
}
