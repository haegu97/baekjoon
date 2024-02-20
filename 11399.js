const fs = require("fs");

let input = fs.readFileSync("input.txt").toString().trim().split("\n");

const line = input[1].split(" ").map(Number);
const sortLine = line.sort((a, b) => a - b);

let ans = 0;
let cur = 0;

sortLine.forEach((l) => {
  ans += l;
  cur += ans;
});

console.log(cur);
