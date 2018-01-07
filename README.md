# Decline Curves 2.Oooh

:construction:


Platform | CI Status 
---------|-------------:
Linux, Python 3.6 | [![Build Status](https://travis-ci.org/plang85/decline_curves_2pointOooh.svg?branch=master)](https://travis-ci.org/plang85/decline_curves_2pointOooh) 


A PyTorch application for next-generation decline curve modelling. The package is named `luibeal`, after the authors (Lewis and Beal) of the 1918 paper.

- Conventional decline curve models are not intended for changing conditions
- Recurrent neural networks (RNN) process temporal data
- Temporal data may be used to represent changes in conditions during a well’s lifetime
- This provides means for a new decline curve modeling framework
- This new framework is able to account for refracking, well interactins and more

PyTorch has chosen a somewhat tight alignment with Anaconda, so this project falls in line given the strong dependency. So standard procedure using a virtual environment
```
conda create -n dcenv
source activate dcenv
conda env update -f environment.yml -n dcenv
python setup.py
```
which creates an environment, activates it, installs dependecies and gets you out of the environment. Optionally you can specify `python setup.py develop` Alternatively, you can create the environment in one go and step into it later, all set up.
```
conda env create -f environment.yml -n dcenv
python setup.py
```
There is also a dockerfile which provided the required development environment - once in the container, cd into the mapped directory and `python setup.py`. Also, no need for GPU, this is kindergarden.
