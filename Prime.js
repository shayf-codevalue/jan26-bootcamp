function printPrimes(n) {
  for (let num = 2; num <= n; num++) {
    let isPrime = true;

    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        isPrime = false;
        break;
      }
    }

    if (isPrime) {
      console.log(num);
    }
  }
}

printPrimes(30);
