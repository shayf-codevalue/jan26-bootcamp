function printPrimes(n) {
  for (let num = 2; num <= n; num++) {
    let isPrime = ;

    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        isPrime = false;
        break;
      }
    }

    if (isPrime) {
      console.log(num);
    }
  <<<
}

// דוגמה
printPrimes(30);
