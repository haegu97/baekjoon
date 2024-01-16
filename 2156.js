const fs = require("fs");
let [n, ...arr] = fs.readFileSync("./dev/stdin").toString().split("\n");

arr = arr.map((num) => parseInt(num));
const dp = new Array(parseInt(n).fill(0));

dp[0] = arr[0];
dp[1] = arr[1] + arr[0];

let case1 = dp[i - 1];
let case2 = dp[i - 2] + arr[i];
let case3 = arr[i] + arr[i - 1] + dp[i - 3];

for (let i = 3; i <= n; i++) {
  dp[i] = Math.max(case1, case2, case3);
}

console.log(dp[n - 1]);
