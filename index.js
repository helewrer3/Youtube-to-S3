const fetch = require("node-fetch");

const f = async (url, filename) => {
  const response = await fetch(`https://xm9ef9rpkc.execute-api.ap-south-1.amazonaws.com/default/lambdas3?filename=${filename}&url=${url}`);
  const data = await response.json();
  console.log(data);
};

//example
f("https://www.youtube.com/watch?v=9j_64DPnnM8", "hb-bad");
