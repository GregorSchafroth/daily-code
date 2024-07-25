// Step 1: Create a JavaScript object
const user = {
  name: "John Doe",
  age: 30,
  city: "New York",
};

console.log("user:", user)

// Step 2: Convert the object to a JSON string
const jsonString = JSON.stringify(user);
console.log("JSON String:", jsonString);

// Step 3: Convert the JSON string back to a JavaScript object
const parsedObject = JSON.parse(jsonString);
console.log("Parsed Object:", parsedObject);
