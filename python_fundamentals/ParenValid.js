function ParenValid(inputstring){
  var leftParen = 0;
  var rightParen = 0;
  for (var i = 0; i < inputstring.length; i++) {
    if (inputstring[0] == ")") {
      return false;
    }
    else if (inputstring[i] == "(") {
      leftParen += 1;
    }
    else if (inputstring[i] == ")") {
      rightParen += 1;
    }
  }
  if (leftParen == rightParen) {
    return true;
  }
  else{
    return false;
  }
}
console.log (ParenValid("Y(3(P)P(3)R)S"))
