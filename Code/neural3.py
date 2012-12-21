# Erin Coughlan and Vivian Wehner
# Neural Network

from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

from getDataSet import *

alldata = get_dataset_txt('test.txt')

# randomly split data into training and testing
tstdata, trndata = alldata.splitWithProportion(0.25)

# info about dataset
print "Number of training patterns: ", len(trndata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0], trndata['class'][0]

# make a feed-forward network with 5 hidden units
fnn = buildNetwork(trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer)

# make the back propogation trainer
trainer = BackpropTrainer(fnn, dataset=trndata)

# training time: 100 total epochs
for i in range(20):
    trainer.trainEpochs(5) # usually a larger number, but 1 for visualization

    # evaluate the network
    trnresult = percentError( trainer.testOnClassData(),
                              trndata['class'] )
    tstresult = percentError( trainer.testOnClassData(
           dataset=tstdata ), tstdata['class'] )

    print "epoch: %4d" % trainer.totalepochs, \
          "  train error: %5.2f%%" % trnresult, \
          "  test error: %5.2f%%" % tstresult

