var Engine = {};

Engine.clusterDataSet = function(matrix, options, cb){
  cb = cb || function (results){
    console.log(results);
  };

  // perform some tests:
  options = options || {};
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
    cb(JSON.parse(output));
  });
};

module.exports = Engine;
