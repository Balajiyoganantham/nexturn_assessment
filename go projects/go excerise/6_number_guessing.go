// Exercise 6: Comprehensive Case Study
// Develop a "Number Guessing Game" that incorporates all the above concepts:
// 1. Data Types and Variables: Declare variables for the target number (integer), number
// of attempts (integer), and user input (integer).
// 2. Conditions: Use conditions to check if the user's guess is correct, too high, or too
// low.
// 3. Loops: Allow the user to keep guessing until they get the correct number or reach a
// maximum number of attempts.
// 4. Functions: Create a function getHint(target, guess int) string that returns a
// hint ("Too high", "Too low", or "Correct").
// 5. Reading User Inputs: Prompt the user to input their guesses.
// 6. Print the result at the end, indicating whether the user won or lost.

package main

import (
	"fmt"
	"math/rand"
)

func main() {
	target := rand.Intn(100) + 1
	var guess int
	maxAttempts := 5

	fmt.Println("Welcome to the Number Guessing Game!")
	fmt.Println("Guess a number between 1 and 100.")

	for attempts := 1; attempts <= maxAttempts; attempts++ {
		fmt.Printf("Attempt %d - Enter your guess: ", attempts)
		fmt.Scan(&guess)

		if guess < target {
			fmt.Println("Too low!")
		} else if guess > target {
			fmt.Println("Too high!")
		} else {
			fmt.Printf("Correct! You guessed the number in %d attempts.\n", attempts)
			return
		}
	}

	fmt.Printf("Sorry! You've used all %d attempts. The correct number was %d.\n", maxAttempts, target)
}
