// Exercise 2: Conditions
// Create a program that determines the type of a triangle based on its sides.
// 1. Input three side lengths as integers.
// 2. Use conditions to check if the triangle is:
// o Equilateral (all sides equal).
// o Isosceles (two sides equal).
// o Scalene (no sides equal).
// 3. Print the type of triangle.

package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Println("Enter the sides of the triangle:")
	fmt.Scanf("%d %d %d", &a, &b, &c)
	if a == b && b == c {
		fmt.Println("The triangle is Equilateral.")
	} else if a == b || b == c || a == c {
		fmt.Println("The triangle is Isosceles.")
	} else {
		fmt.Println("The triangle is Scalene.")
	}
}
