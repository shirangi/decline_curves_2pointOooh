# Decline Curves 2.Oooh

- Conventional decline curve models cannot account for changing conditions
- Recurrent neural networks (RNN) process temporal data
- Temporal data may be used to represent changes in conditions during a well’s lifetime
- This provides means for a new decline curve modeling framework
- This new framework is able to account for refracking, well interactins and more

PyTorch has chosen a somewhat tight alignment with Anaconda, so this project falls in line given the strong dependency. So standard procedure 
```
conda create -n dcenv
source activate dcenv
conda env update -f environment.yml
source deactivate dcenv
```
which creates an environment, activates it, istalls dependecies and gets you out of the environment. Alternatively, you can create the environment in one go and step into it later, all set up.
```
conda env create -f environment.yml
```
No need for Cuda support, this is kindergarden.