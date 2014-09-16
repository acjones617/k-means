var eng = require('./node/engine');

module.exports = function(matrix, options, cb) {
  eng.clusterDataSet(matrix, options, cb);
}
