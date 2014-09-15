// var rec = require('./variables').rec;
var Engine = {};

Engine.clusterDataSet = function(matrix, cb, options){
  cb = cb || function(){};

  // perform some tests:
  options.iterations = options.iterations || 10

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
    cb(output);
    // _buildRecVariables(output);
    // args = Array.prototype.slice.call(arguments,4);
    // cb.apply(this,args);
  });
};

module.exports = Engine;