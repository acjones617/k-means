var Engine = {};

Engine.clusterDataSet = function(matrix, options, cb){
  if (typeof options === 'function') {
    cb = options;
    options = undefined;
  }

  cb = cb || function (results){
    console.log(results);
  };

  options             = options            || {};
  options.clusters    = options.clusters   || 2;
  options.iterations  = options.iterations || 10;
  options.assigned    = options.assigned ? 1 : 0;
  
  // perform some tests:
  if (!Array.isArray(matrix) || !Array.isArray(matrix[0])) {
    throw 'Need to input a 2-dimensional array for clustering';
  }

  matrix = JSON.stringify(matrix);
  options = JSON.stringify(options);

  var python = require('child_process').spawn(
    'python',
    [__dirname + '/../lib/exec.py', matrix, options]);
  output = '';
  python.stdout.on('data', function(data){
    output += data;
  });
  python.stdout.on('close', function(){
    cb(JSON.parse(output));
    // cb(output);
  });
};

module.exports = Engine;
