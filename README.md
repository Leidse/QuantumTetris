# QuantumTetris
A solution for utilizing quantum in order to optimize the load on a defined area


## Requirements
Python3.6+
<br>qiskit-aqua 0.4.1
<br>setuptools 39.1.0
<br>cloudpickle 0.5.6
<br>flask 1.0.2

## Common issuses
#### errors when installing qiskit-aqua via cmd
This has to do with the setup.py and requirements of qiskit you are trying to install.
When using the package installer from pycharm 2018.2 the right installations will be used.

### Windows:
### pycharm
#### pip.main does not exist (when installing package)
This has to do with the installed interpeter of pycharm.
The newest version of pycharm (pycharm 2018.2) is adviced in combination with python 3.7

#### ImportError: DLL load failed (when import cvxopt.base)
This happens when your system can not find the right mkl connection.
You can fix this by adding C:\Users\you\Python\Library\bin\ to your path.

## Authors
Kiet van Osnabrugge
<br>Tom van Hamersveld

