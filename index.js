const fetch = require("node-fetch");

const f = async (url) => {
  const response = await fetch(`https://src3vh3i7c.execute-api.ap-south-1.amazonaws.com/default/lambdas3-node?url=${url}`);
  const data = await response.json();
  console.log(data);
};

//example
f("https://www.youtube.com/watch?v=9Qep0ImvVHg");
