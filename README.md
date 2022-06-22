# CPP
Python implementation of Cepstral Peak Prominence (CPP)

## Demo
- `cpp_demo.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satvik-dixit/CPP/blob/main/cpp_demo.ipynb) is the demo for using the python implementation of CPP
- `cpp_single_window.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satvik-dixit/CPP/blob/main/cpp_single_window.ipynb) is the demo for using the python implementation for CPP (using only a single window)

## Function
- `cpp.py` is the function for getting CPP

## Matlab implementation 
`cpp_matlab_implementation` folder contains the matlab implementation of CPP. It contains:
- `cpp_function.m` contains matlab implementation of CPP (taken from https://github.com/covarep/covarep/blob/master/glottalsource/cpp.m)
- `cpp_plot.m` contains matlab code for getting single window CPP and making plots

## Demos for using other methods to get cepstrum 
- `cpp_vfp_demo.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satvik-dixit/CPP/blob/main/ccpp_vfp_demo.ipynb) is the demo for single window CPP using a different method to get cepstrum and comparing results with praat 
- `cepstrum_methods.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satvik-dixit/CPP/blob/main/cepstrum_methods.ipynb) demonstrates different ways of getting cepstrums (and therefore CPPs)

## Other folders
- `audio_files` folder contains all the audio files used in the demos
- `images` folder contains the plots from matlab and praat for all the audio files
- `files` folder contains `CPP_example_values.csv` which has the matlab implementation cpp values for all the audio files

## References
1. Fraile, R., & Godino-Llorente, J. I. (2014). Cepstral peak prominence: A comprehensive analysis. Biomedical Signal Processing and Control, 14, 42-54.
2. Murton, O., Hillman, R., & Mehta, D. (2020). Cepstral peak prominence values for clinical voice evaluation. American Journal of Speech-Language Pathology, 29(3), 1596-1607.
3. https://github.com/covarep/covarep/blob/master/glottalsource/cpp.m