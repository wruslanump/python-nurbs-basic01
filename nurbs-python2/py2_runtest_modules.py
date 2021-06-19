#! /usr/bin/env python
"""
File  : py2_runtest_modules.py 
Author: wruslandr@gmail.com

wruslan@HPEliteBk8470p-ubstudio-20:~$ date
Wed 16 Jun 2021 08:00:39 PM +08

wruslan@HPEliteBk8470p-ubstudio-20:~$ uname -a
Linux HPEliteBk8470p-ubstudio-20 5.10.25-rt35 
#3 SMP PREEMPT_RT Wed Apr 7 12:33:26 +08 2021 x86_64 x86_64 x86_64 GNU/Linux
 
wruslan@HPEliteBk8470p-ubstudio-20:~$ lsb_release -a
LSB Version:	core-11.1.0ubuntu2-noarch:security-11.1.0ubuntu2-noarch
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.2 LTS
Release:	20.04
Codename:	focal
wruslan@HPEliteBk8470p-ubstudio-20:~$ 

===========================================================
SUCCESS EXECUTION $ python runtest-python2-modules.py 
===========================================================
wruslan@HPEliteBk8470p-ubstudio-20:~/github/wruslanump/python-csv-pandas-data-processing/python2-files$ python runtest-python2-modules.py 
2021-06-17 02:23:46.749385 ==>  Starting:  runtest-python2-modules.py ==> Bismillah Hirrahma Nirrahim in python2.7
2021-06-17 02:23:49.702353 ==>  Completed: runtest-python2-modules.py ==> Alhamdulillah Hirrabil Alamin in python2.7
2021-06-17 02:23:49.702465 ==>  Duration: 2.953086 seconds execution for the total execution time of runtest-python2-modules.py
wruslan@HPEliteBk8470p-ubstudio-20:~/github/wruslanump/python-csv-pandas-data-processing/python2-files$ 

"""
## IMPORTS FOR SYSTEM-DEFINED MODULES
## For python time stamp
import time
from datetime import datetime

## IMPORTS FOR USER-DEFINED MODULES
import sys
sys.path.insert(0, './py2modules')
import py2_datetimestamp as P2DTS

## CAPTURE THE START TIME TO CALCULATE THE EXECUTION DURATION LATER
tstart1 = datetime.now()
P2DTS.datetimestamp_us("Starting:  py2_runtest_modules.py ==> Bismillah Hirrahma Nirrahim in python2.7")

### =======================================================

### BASIC SYSTEM PACKAGES

import sys          #(Access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.)
import os           #(Automatically perform many operating system tasks, creating and removing a directory (folder), fetching its contents, etc)
import time         #(Provides many ways of representing time in code, such as objects, numbers, and strings.) 
import datetime     #(Module supplies classes to work with date and time.)
import dateutil     #(Built-in datetime module which is used for manipulating dates and times from simple to complex ways.) 
import errno        #(Module defines a number of symbolic error codes, such as ENOENT 

### MATHEMATICAL PACKAGES

import numpy           #(NumPy is the fundamental package for array computing with Python.)
import scipy           #(SciPy: Scientific Library for Python)  
import random          #(Python 2 random module.)
import random2         #(Python 3 compatible Python 2 random module.)
import math            #(Module provides functions useful in number theory as well as in representation theory, a related field.)
import cmath           #(Complex number is a combination of a real number and an imaginary number.) 
import decimal         #(Decimal module for fast correctly-rounded decimal floating point arithmetic. The exactness carries over into arithmetic.)
import fractions       #(Rational number arithmetic. Allows to create a Fraction instance from integers, floats, numbers, decimals and strings.) 
import statistics      #(Python's statistics is a built-in Python library for descriptive statistics. Not too large numbers) 
import string          #(Module contains a single utility function - capwords(s, sep=None). This function split the specified string into words using str.) 
import StringIO        #(An in-memory file-like object. Object can be used as input/output to most function that would expect a standard file object.
import mpmath          #(Python library for real and complex floating-point arithmetic with arbitrary precision)

### EXECUTION PROCESSING

import mpi4py           #(Python bindings for the Message Passing Interface (MPI). API which grounds on the standard MPI-2 C++ bindings.)
import threading        #(Threading in python is used to run multiple threads (tasks, function calls) at the same time.)
import multiprocessing  #(Multiprocessing supports spawning processes using an API. Can fully leverage multiple processors on a given machine.)
import concurrent       #(Launching parallel tasks. )
import trace            #(Trace or track Python statement execution. It can be used in another program or from the command line.)
import traceback        #(standard interface to extract, format and print stack traces of Python programs.) 
import traceback2       #(In Python 2.x, unlike traceback, traceback2 creates unicode output)

### GRAPHICS PROCESSING PACKAGES

import geomdl      #(Python-NURBS library)
import plotly      #(Plotting library)
import matplotlib.pyplot
import matplotlib  #(Plotting library for Python and NumPy. Object-oriented API embedding plots using GUI toolkits Tkinter, wxPython, Qt, or GTK.)
import pylab       #(Module that bulk imports matplotlib.pyplot (for plotting) and NumPy (for Mathematics) in a single name space.)
import Gnuplot     #(Python package that interfaces to gnuplot. Can plot data on the fly as they are computed.)
import PyGnuplot   #(PyGnuplot: Python wrapper for Gnuplot.)
import pygnuplot   #(Python wrapper for Gnuplot.) 
import graphviz    #(Graphviz module used to create graph objects which can be completed using different nodes and edges.)
import PyPDF2      #(Python program to dynamically generate a graph, digraph in Graphviz's Dot.)
import pydot       #(pydot.PyPI - Python interface to Graphviz's Dot.)
import pydotplus   #(PyDotPlus is an improved version of the old pydot project.)
import tkinter     #(Tkinter is the de facto way in Python to create Graphical User interfaces - GUIs) 
import PyQt4       #(PyQt4 is a comprehensive set of Python bindings for Digia's Qt cross platform GUI toolkit.) 
import PyQt5       #(PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules)

### FILE PROCESSING PACKAGES

import io          #(Python io module allows us to manage the file-related input and output operations. Can write to Unicode data)
import fileinput   #(Module can iterate over lines from multiple input streams, write a loop over standard input or a list of files, etc)
import difflib     #(Module provides classes and functions for comparing sequences. Can be used for comparing files, file differences, etc) 
import filecmp     #(Module defines functions to compare files and directories, with various optional time/correctness trade-offs.)
import FileDialog  #(File selection dialogs. The tkinter.filedialog module provides classes for creating file/directory selection windows).
import h5py        #(H5PY package is a Pythonic interface to the HDF5 binary data format. For example: Scilab/Octave data outputs/inputs)
import FileDialog  #(File selection dialogs. The tkinter.filedialog module provides classes for creating file/directory selection windows).

### DATA PROCESSING PACKAGES

import hdf5storage #(Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.)
## import h5df     #(Python library and CLI for storing large numeric data frames in HDF5.)
import csv         #(Comma Separated Values - most common import and export format for spreadsheets and databases.)
import pandas      #(Python Data Analysis - imports data various file formats like comma-separated values, JSON, SQL, Microsoft Excel.)
import seaborn     #(Python Data Visualization - attractive and informative statistical graphics, Matplotlib-based.)


### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P2DTS.datetimestamp_us("Completed: py2_runtest_modules.py ==> Alhamdulillah Hirrabil Alamin in python2.7")
P2DTS.execution_duration(tstart1, "for the total running time of py2_runtest_modules.py")

"""
===========================================================
ALHAMDULILLAH 3 TIMES.
===========================================================
"""

