var eng = require('./engine');

eng.clusterDataSet([
  [0,0,0],
  [0,1,1],
  [1,0,1],
  [1,1,0],
  [22.1,22,1]], function (results) {
  console.log('in callback')
  console.log(results);
}, {clusters: 2});

