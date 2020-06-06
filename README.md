# GDoeSII 

(C) 2019-2021 Raghu Dharmavarapu. This is free software, released under the CC - BY - NC 4.0 license.

GDoeSII can compute scalar diffraction patterns of a given input phase and amplitude profile. It can also convert the phase
profiles into GDSII layouts for further lithography/fabrication process.

# Setup and requirements python 3.x 

The Python code is for Python 3.x. The following packages must be installed before running the source code.
1. gdsCAD 
** Note ** The current gdsCAD from PyPI wont support Python 3.0. You must build and install the python 3 compatible gdsCAD from github
from the following link.
https://github.com/hohlraum/gdsCAD/tree/2and3. 
Steps: a. Clone the repo.
       b. Do git branch -r to see all branches.
       c. Checkout to the branch named '2and3'
       d. Run the following command python setup.py install
2. Numpy
3. Scipy
4. Matplotlib
5. PIL
6. tkinter
7. imageio

The source files can be found in the src folder. The main python file of the software is GDoeSII.py, which contains all the code for GUI and framework of the software. 

** Optional: Pyisntaller package can be usesd to build a single EXE file for the tool. The necessary commands and configuration files are in config/ directory. **
