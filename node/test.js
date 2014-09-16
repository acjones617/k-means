var eng = require('./engine');

eng.clusterDataSet([
  [0,0,0],
  [0,1,1],
  [1,0,1],
  [1,1,0],
  [22.1,22,1]], function (results) {
  console.log('in callback')
  // console.log(results);
  // console.log(typeof results)
  for (var i = 0; i < results.length; i++) {
    console.log(results[i])
  }
}, {clusters: 2, iterations: 4});

