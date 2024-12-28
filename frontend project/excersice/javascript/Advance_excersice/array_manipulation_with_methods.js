
let arr = [1, 2, 3];
arr.push(4);
console.log("After push(4):", arr);
arr.pop();
console.log("After pop():", arr); 
arr.unshift(0);
console.log("After unshift(0):", arr);
arr.shift();
console.log("After shift():", arr); 
console.log("Using forEach to iterate over the array:");
arr.forEach(function(element) {
    console.log(element);
});
