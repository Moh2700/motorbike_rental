function isValidEmail(strvalue) {
  // Regular expression for validating an Email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  return emailRegex.test(strvalue);
}

function isValidLetter(strvalue) {
  return /^[A-Za-z ]+$/.test(strvalue);
}
