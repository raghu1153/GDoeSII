# GDoeSII 

(C) 2019-2021 Raghu Dharmavarapu. This is free software, released under the CC - BY - NC 4.0 license.

GDoeSII can compute scalar diffraction patterns of a given input phase and amplitude profile. It can also convert the phase
profiles into GDSII layouts for further lithography/fabrication process.

# Setup and requirements python 2.7. (For Python 3 checkout the other git branch)

The Python code is for Python 2.7. The following packages must be installed before running the source code.
1. gdsCAD 
2. Numpy
3. Scipy
4. Matplotlib
5. PIL
6. xlrd

The source files can be found in the src folder. The main python file of the software is GDoeSII.py, which contains all the code for GUI and framework of the software. 

** Optional: Pyisntaller package can be usesd to build a single EXE file for the tool. The necessary commands and configuration files are in config/ directory. **
