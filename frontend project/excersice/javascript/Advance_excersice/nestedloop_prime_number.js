// Function to check and print prime numbers within a range
function findPrimeNumbers(max) {
    console.log(`Prime numbers up to ${max}:`);

    for (let num = 2; num <= max; num++) {
        let isPrime = true; // Assume the number is prime

        // Check for factors from 2 to the square root of num
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                isPrime = false; // Found a divisor, not prime
                break; // Exit the inner loop early
            }
        }

        // If isPrime is still true, num is a prime number
        if (isPrime) {
            console.log(num);
        }
    }
}

// Example usage: Find prime numbers up to 100
findPrimeNumbers(100);
