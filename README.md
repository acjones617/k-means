# k-means NPM Module
=======
## <a name='contents' href='#'/> Contents

[What is k-means?](#about)  
[Setup Process](#setup)  
[API](#use)

## <a name='about' href='#'/>  What is k-means?

k-means is an npm module that utlizes python under the hood to give easy access to running a k-means clustering algorithm on your dataset. k-means exists on the npm registry under the name "k-means". The code can be seen at my <a href='https://github.com/acjones617/k-means'>k-means</a> github repo. A demo application of the k-means clustering algorithm is forthcoming.
    
    npm install --save k-means

The algorithm in the lib folder uses unsupervised machine learning k-means algorithm to cluster similar data samples together.  The algorithm expects the data to be clustered to be structured as a matrix. This should be represented in JavaScript as a two-dimensional array: each inner-array is a sample of the data, while each element inside the inner-array is a feature of that sample. The features should line up accordingly. In other words, the 2nd feature of the 3rd sample should represent the same feature, as well as using the same units as, the 2nd feature of the 112th sample. 

The number of desired clusters to cluster the data into should also be inputted. The algorithm divides the data into n distinct clusters.

Using the node.js command line interface, the underlying python engine can be launched as a child process, with the results streamed to node. These results are divided into various variables based on the type of data they hold, and a user can gain access to all this raw analysis.

## <a name='setup' href='#'/> Setup Process

To utilize the Product-Recommender NPM module, the first step would be to make sure one has successfully installed node.js, npm, and a python version of >= 2.7.  To install these items, I would recommend you check out http://nodejs.org/download/ and https://www.python.org/download/.

In addition to these prerequisites, you will need to install a few python modules: numpy and jsonpickle. For install instructions on numpy, please go to http://www.scipy.org/install.html. For jsonpickle, please look at http://jsonpickle.github.io/#download-install. Some more python modules used in this project are argparse, ast, math, and random, though these should be included in the Python Standard Library so there is likely no need to download these.

## <a name='use' href='#'/> API

To use my k-means algorithm, first install k-means:

    npm install --save k-means

Then, require k-means in your js file. I'm going to use the variable 'cluster' to represent the k-means library

    var cluster = require('k-means');

cluster is a function that takes up to three arguments

### matrix (required)

As mentioned above, our matrix should be represented in JavaScript as a two-dimensional array: each inner-array is a sample of the data, while each element inside the inner-array is a feature of that sample. The features should line up accordingly. In other words, the 2nd feature of the 3rd sample should represent the same feature, as well as using the same units as, the 2nd feature of the 112th sample.

    var matrix = [[1, 1, 3], [4, 5, 1], [6, 5, 2]]

### options (optional)

Here, you can customize how you want your k-means clustering to run. Our options object can take up to two properties:

    var options = {
      clusters: 2 // number of clusters we want to cluster our data into. The default is 2. Sometimes, it is natural for one or more clusters to end up being excluded if they would not contain any data points.
      iterations: 10 // number of iterations we want our k-means to run. The higher the number, the potentially more accurate, but it might take longer. The algorithm will cut off early if clusters stay perfectly consistent between iterations.
    }

### callback (optional)

The results of the k-means clustering will be passed to a provided callback function

    var callback = function (results){
      console.log(results)
    }

The passed-in results object contains two pieces of data: finalMatrix and clusterCenters.

finalMatrix will be similar to your original matrix you passed in, except where each index in your original array is a sample of your data, each index of finalMatrix will be an array with two elements: the first one being the cluster that the sample is assigned to, the second being the sample itself. The order of samples will remain the same.

clusterCenters is an array of length = number of clusters, where each index is the center coordinates of that cluster. The index of clusterCenters matches up to the cluster number assigned to each sample in finalMatrix.