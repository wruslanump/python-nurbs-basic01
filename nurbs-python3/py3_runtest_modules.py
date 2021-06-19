#! /usr/bin/env python3
"""
File  : py3_runtest_modules.py 
Author: wruslandr@gmail.com

wruslan@HPEliteBk8470p-ubstudio-20:~$ date
Wed 16 Jun 2021 11:19:35 PM +08

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
"""
## IMPORTS FOR SYSTEM-DEFINED MODULES
## For python time stamp
import time
from datetime import datetime

## IMPORTS FOR USER-DEFINED MODULES
import sys
sys.path.insert(0, './py3modules')
import py3_datetimestamp as P3DTS


## CAPTURE THE START TIME TO CALCULATE THE EXECUTION DURATION LATER
tstart1 = datetime.now()
P3DTS.datetimestamp_us("Starting:  py3_runtest_modules.py ==> Bismillah Hirrahma Nirrahim in python3.8")

### BASIC SYSTEM PACKAGES

import sys          #(Access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.)
import os           #(Automatically perform many operating system tasks, creating and removing a directory (folder), fetching its contents, etc)
import time         #(Provides many ways of representing time in code, such as objects, numbers, and strings.) 
import datetime     #(Module supplies classes to work with date and time.)
import dateutil     #(Built-in datetime module which is used for manipulating dates and times from simple to complex ways.) 
import errno        #(Module defines a number of symbolic error codes, such as ENOENT (no such directory entry) and EPERM (permission denied). )

### MATHEMATICAL PACKAGES

import numpy           #(NumPy is the fundamental package for array computing with Python.) 
import scipy           #(SciPy: Scientific Library for Python)
import random          #(Python 2 random module.)
import random2         #(Python 3 compatible Pytohn 2 random module.)
import math            #(Module provides functions useful in number theory as well as in representation theory, a related field.)
import cmath           #(Complex number is a combination of a real number and an imaginary number.) 
import fractions       #(Rational number arithmetic. Allows to create a Fraction instance from integers, floats, numbers, decimals and strings.) 
import statistics      #(Python's statistics is a built-in Python library for descriptive statistics. Not too large numbers) 
import string          #(Module contains a single utility function - capwords(s, sep=None). This function split the specified string into words using str.) 
import mpmath          #(Python library for real and complex floating-point arithmetic with arbitrary precision)
from io import StringIO  #(StringIO is a in-memory file-like object. Object can be used as input/output ...)
import io              #(Python io module allows us to manage the file-related input and output operations. Can write to Unicode data)

### EXECUTION PROCESSING

import mpi4py              #(Python bindings for the Message Passing Interface (MPI). API which grounds on the standard MPI-2 C++ bindings.)
import threading           #(Threading in python is used to run multiple threads (tasks, function calls) at the same time.)
import multiprocessing     #(Multiprocessing supports spawning processes using an API. Can fully leverage multiple processors on a given machine.)
import concurrent          #(Launching parallel tasks.)
import trace               #(Trace or track Python statement execution. It can be used in another program or from the command line.)
import traceback           #(standard interface to extract, format and print stack traces of Python programs.) 
import traceback2          #(In Python 2.x, unlike traceback, traceback2 creates unicode output)
import Concurrent_AP       #(Scalable and parallel programming implementation of Affinity Propagation clustering)
import parallel_transform  #(An implementation of asynchronous multiprocessing with progress logging.)
import pytest_parallel     #(A pytest plugin for parallel and concurrent testing)

### GRAPHICS PROCESSING PACKAGES

import geomdl      #(Python NURBS library)
import plotly      #(Plotting Library)
import matplotlib  #(Plotting library for Python and NumPy. Provides object-oriented API embedding plots using GUI toolkits Tkinter, wxPython, Qt, or GTK.)
import Gnuplot     #(Python package that interfaces to gnuplot. Can plot data on the fly as they are computed.)
import PyGnuplot   #(PyGnuplot: Python wrapper for Gnuplot.)
import pygnuplot   #(Python wrapper for Gnuplot.) 
import graphviz    # (Graphviz module used to create graph objects which can be completed using different nodes and edges.)
import pydot       #(pydot.PyPI - Python interface to Graphviz's Dot.)
import pydotplus   #(PyDotPlus is an improved version of the old pydot project.)
import tkinter     #(Tkinter is the de facto way in Python to create Graphical User interfaces - GUIs) 
import PyQt5       # (PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules)
import PyPDF2      #(Python program to dynamically generate a graph, digraph in Graphviz's Dot.)
import PyPDF3      #(A Pure-Python library built as a PDF toolkit)
import PyPDF4      #(A Pure-Python library built as a PDF toolkit)
import landscape_pdf

### FILE PROCESSING PACKAGES

import io          #(Python io module allows us to manage the file-related input and output operations. Can write to Unicode data)
import fileinput   #(Module can iterate over lines from multiple input streams, write a loop over standard input or a list of files, etc)
import difflib     #(Module provides classes and functions for comparing sequences. Can be used for comparing files, file differences, etc) 
import filecmp     #(Module defines functions to compare files and directories, with various optional time/correctness trade-offs.)

### DATA PROCESSING PACKAGES

import h5py        #(H5PY package is a Pythonic interface to the HDF5 binary data format. For example: Scilab/Octave data outputs/inputs)
import hdf5storage #(Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.)
import h5df        #(Python library and CLI for storing large numeric data frames in HDF5.)
import csv         #(Comma Separated Values - most common import and export format for spreadsheets and databases.)
import pandas      #(Python Data Analysis - imports data various file formats like comma-separated values, JSON, SQL, Microsoft Excel.)
import seaborn     #(Python Data Visualization - attractive and informative statistical graphics, Matplotlib-based.)
import vitables    #(ViTables is a graphical tool for browsing and editing files in both PyTables and HDF5 format)

### DEEP LEARNING NEURAL NETWORKS

import tensorflow   #(TensorFlow is one of the most famous machine learning libraries)
import keras        #(Keras is best for easy and fast prototyping as a deep learning library.)
import torch        #(The package name for PyTorch is torch. With strong GPU acceleration.)
import torchvision  #(Image and video datasets and models for torch deep learning)

### WE CALCULATE DURATION SINCE START-TIME. NO NEED TO CAPTURE END-TIME AND SENT TO THE MODULE. 
### THE DATE-TIME STAMP MODULE CAPTURES AUTOMATICALLY END-TIME FROM THE SYSTEM CLOCK AS IT EXECUTES.
P3DTS.datetimestamp_us("Completed: py3_runtest_modules.py ==> Alhamdulillah Hirrabil Alamin")
P3DTS.execution_duration(tstart1, "for the total running time")

"""
===========================================================
ALHAMDULILLAH 3 TIMES.
===========================================================

wruslan@HPEliteBk8470p-ubstudio-20:~/github/wruslanump/python-nurbs-temp/nurbs-python3$ ls -al
total 60
drwxrwxr-x 3 wruslan wruslan 4096 Jun 20 02:11 .
drwxrwxr-x 5 wruslan wruslan 4096 Jun 20 01:50 ..
drwxrwxr-x 2 wruslan wruslan 4096 Jun 20 02:07 py3modules
-rw-rw-r-- 1 wruslan wruslan 8742 Jun 20 02:11 py3_runtest_modules.py
-rw-rw-r-- 1 wruslan wruslan 2046 Jun 20 01:47 test01.py
-rw-rw-r-- 1 wruslan wruslan  357 Jun 20 00:49 test02.py
-rw-rw-r-- 1 wruslan wruslan  296 Jun 20 00:51 test03.py
-rw-rw-r-- 1 wruslan wruslan  425 Jun 20 00:52 test04.py
-rw-rw-r-- 1 wruslan wruslan  269 Jun 20 00:53 test05.py
-rw-rw-r-- 1 wruslan wruslan  424 Jun 20 00:55 test06.py
-rw-rw-r-- 1 wruslan wruslan  345 Jun 20 00:57 test07.py
-rw-rw-r-- 1 wruslan wruslan  310 Jun 20 00:58 test08.py
-rw-rw-r-- 1 wruslan wruslan  910 Jun 20 00:59 test09.py
wruslan@HPEliteBk8470p-ubstudio-20:~/github/wruslanump/python-nurbs-temp/nurbs-python3$

wruslan@HPEliteBk8470p-ubstudio-20:~/github/wruslanump/python-nurbs-temp/nurbs-python3$ python3 py3_runtest_modules.py 
2021-06-20 02:16:21.073424 ==>  Starting:  py3_runtest_modules.py ==> Bismillah Hirrahma Nirrahim in python3.8
2021-06-20 02:16:23.259436: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
2021-06-20 02:16:24.986856 ==>  Completed: py3_runtest_modules.py ==> Alhamdulillah Hirrabil Alamin
2021-06-20 02:16:24.986917 ==>  Duration: 3.913499 seconds execution for the total running time
wruslan@HPEliteBk8470p-ubstudio-20:~/github/wruslanump/python-nurbs-temp/nurbs-python3$ 

"""

