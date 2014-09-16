var eng = require('./engine');

eng.clusterDataSet([
  [0,0,0],
  [0,1,1],
  [1,0,1],
  [1,1,0],
  [22.1,22,1]], {clusters: 2, iterations: 4});

