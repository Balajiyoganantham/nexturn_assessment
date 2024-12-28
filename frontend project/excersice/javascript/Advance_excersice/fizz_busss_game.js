// FizzBuzz function
function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
        // Check for multiples of both 3 and 5
        if (i % 3 === 0 && i % 5 === 0) {
            console.log("FizzBuzz");
        }
        // Check for multiples of 3
        else if (i % 3 === 0) {
            console.log("Fizz");
        }
        // Check for multiples of 5
        else if (i % 5 === 0) {
            console.log("Buzz");
        }
        // If not a multiple of 3 or 5, print the number
        else {
            console.log(i);
        }
    }
}

// Call the function to run FizzBuzz
fizzBuzz();
