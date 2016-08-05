# The CERN@school Coding Challenges

This repository contains a series of Jupyter Notebooks featuring challenges
and code related to the analysis of CERN@school data.

* [Challenge 01: Particle Counting](./01_particle_counting.ipynb).

## Required software
To use these notebooks, you'll need a system capable of running
[Jupyter notebooks](http://jupyter.org/).
We recommend installing
[Anaconda](https://www.continuum.io/downloads),
which will give you all of the Python software you'll need to get stuck
into open data science and analysis with CERN@school.

You can download Anaconda (or Miniconda) for free
[here](https://www.continuum.io/downloads).

### Running on a CernVM
Anaconda and the CERN@school software has been tested on the
GridPP CernVM, a virtual machine image based on the
Scientific Linux 6 operating system.
While it is possible to run everything on Windows and Mac,
we cannot provide support for running natively on these operating
systems.

You can find instructions for creating and running a
GridPP CernVM
[here](https://www.gridpp.ac.uk/userguide/gridpp-cernvm/gridpp-cernvm.html).
Once you're up and running, you can install Anaconda/Miniconda
as above.

### Required packages
Once you've got Anaconda/Miniconda, you'll need to install the
following packages with the following command:

```bash
$ conda install scipy matplotlib pandas jupyter
```

(Though they may well be installed already.)

## Getting and running the code
While you can view the challenge notebooks in the browser by clicking
on the links above, the real power of the notebooks comes from
cloning them (or forking the repository) and interacting with them
via the Jupyter Notebook platform as follows:

```bash
$ cd ~
$ export MY_WORKING_DIRECTORY=tmp # or whatever you want to call it.
$ mkdir $MY_WORKING_DIRECTORY
$ cd $MY_WORKING_DIRECTORY
$ git clone https://github.com/twhyntie/coding-challenges.git
$ cd coding-challenges
$ jupyter notebook
```

A web browser should now open up and display a list of the
notebooks containing the challenges. Simply click on the notebook
you want to get working on to open it in a new browser tab.

Good luck!

## Getting help
If you run into problems, please raise an issue on the repository's
[issue page](./issues). We'll do our best to help if we can!

## Further information
See the [CERN@school homepage](http://researchinschools.org/CERN) for more information
and to find out how you can get involved.

This work was supported by
[STFC](http://www.stfc.ac.uk) Public Engagement Fellowship
grant number ST/N00101X/1.

_CERN@school is a flagship programme of the
[Institute for Research in Schools](http://researchinschools.org)_.
