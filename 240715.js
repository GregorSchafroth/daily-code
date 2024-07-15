// Exercise: Palindrome Checker
// Objective: Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

function is_palindrome(string){
  string = string.trim();
  for (let i = 0; i < string.length; i++){
    if (string[i].toLowerCase() !== string[(string.length - 1 - i)].toLowerCase()) {
      return false
    }
  }
  return true
}

console.log(is_palindrome('Anna'))
console.log(is_palindrome('Washington'))