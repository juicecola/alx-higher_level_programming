#!/usr/bin/node

const args = process.argv.slice(2);

const findSecondLargest = (arr) => {
  if (arr.length < 2) {
    return 0;
  }
  let largest = arr[0];
  let secondLargest = arr[1];
  if (secondLargest > largest) {
    [largest, secondLargest] = [secondLargest, largest];
  }
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] > largest) {
      secondLargest = largest;
      largest = arr[i];
    } else if (arr[i] > secondLargest) {
      secondLargest = arr[i];
    }
  }
  return secondLargest;
};

const intArgs = args.map(x => parseInt(x, 10));

console.log(findSecondLargest(intArgs));
