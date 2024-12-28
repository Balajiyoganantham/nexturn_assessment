// Create a multi-dimensional array (2D array)
let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Access elements from the multi-dimensional array
console.log("Element at [0][0]:", matrix[0][0]); // 1
console.log("Element at [1][2]:", matrix[1][2]); // 6

// Iterate over the 2D array using forEach
console.log("Iterating over the 2D array:");
matrix.forEach(function(row) {
    row.forEach(function(element) {
        console.log(element);
    });
});
