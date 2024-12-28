// Exercise 3: Loops
// Write a program to calculate the factorial of a number.
// 1. Input an integer from the user.
// 2. Use a loop to calculate the factorial.
// 3. Print the result.

package main

import "fmt"

func main() {
	var num int
	fmt.Print("Enter a number: ")
	fmt.Scanf("%d", &num)
	factorial := 1
	for i := 1; i <= num; i++ {
		factorial *= i
	}
	fmt.Printf("Factorial of %d is %d\n", num, factorial)
}
