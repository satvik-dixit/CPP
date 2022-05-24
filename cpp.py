import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from sklearn.linear_model import LinearRegression
import scipy.io.wavfile
import io
from IPython.display import Image



# function for computing cepstral peak prominence

def cpp_function(x, fs, pitch_range, trendline_quefrency_range):
    """
    Computes cepstral peak prominence for a given signal 

    Parameters
    -----------
    x: ndarray
        The audio signal
    fs: integer
        The sampling frequency
    pitch_range: list of 2 elements
        The pitch range where a peak is searched for
    trendline_quefrency_range: list of 2 elements
        The quefrency range for which the amplitudes will be modelled by a straight line

    Returns
    -----------
    integer
        The cepstral peak prominence of the audio signal
    """
    # Cepstrum
    x = np.hamming(len(x))*x
    spectrum = np.fft.rfft(x)
    spectrum = 20*np.log10(np.abs(spectrum))
    ceps = np.fft.rfft(spectrum)
    ceps = 20*np.log10(np.abs(ceps))

    # Quefrency
    dt = 1/fs
    freq_vector = np.fft.rfftfreq(len(x), d=dt)
    df = freq_vector[1] - freq_vector[0]
    quefrency_vector = np.fft.rfftfreq(2*ceps.size-2, df)

    # Selecting part of cepstrum
    quefrency_range = [1/pitch_range[1], 1/pitch_range[0]]
    index_range = np.where((quefrency_vector >= quefrency_range[0]) & (
        quefrency_vector <= quefrency_range[1]))

    # For trend line
    index_range_tl = np.where((quefrency_vector >= trendline_quefrency_range[0]) & (
        quefrency_vector <= trendline_quefrency_range[1]))

    # Linear regression
    linear_regressor = LinearRegression()
    linear_regressor.fit(
        quefrency_vector[index_range_tl].reshape(-1, 1), ceps[index_range_tl].reshape(-1, 1))
    Y_pred = linear_regressor.predict(quefrency_vector.reshape(-1, 1))

    # CPP
    peak_value = np.max(ceps[index_range])
    peak_index = np.argmax(ceps[index_range])
    cpp = peak_value - Y_pred[index_range][peak_index][0]

    return cpp

