
// IIFE - Immediately Invoked Function Expression

(function someFunction() {

}())


// Recursive function call

function someFunction() {
  someFunction();
}

// Asynchronous Recursive function call

function main() {
  // DO some stuff with the canvas
  requestAnimationFrame(main);
}
