// Exercise: Palindrome Checker
// Objective: Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

function is_palindrome(string){
  string = string.trim().toLowerCase().replace(/[^a-z0-9]/g, '');
  for (let i = 0; i < Math.floor(string.length / 2); i++){
    if (string[i] !== string[(string.length - 1 - i)]) {
      return false
    }
  }
  return true
}

// test cases
console.log(is_palindrome('Anna')); // Should return true
console.log(is_palindrome('Washington')); // Should return false
console.log(is_palindrome('A man, a plan, a canal, Panama')); // Should return true
console.log(is_palindrome('No lemon, no melon')); // Should return true