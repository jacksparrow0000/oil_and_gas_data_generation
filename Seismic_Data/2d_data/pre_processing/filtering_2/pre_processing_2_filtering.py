import pandas as pd

# Load the seismic data
csv_file_path = 'synthetic_2d_seismic_corrected_data.csv'  # Update this with the path to your CSV file
seismic_data = pd.read_csv(csv_file_path)

from scipy.signal import butter, sosfiltfilt
import numpy as np

# Function to create a band-pass filter
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], btype='band', output='sos')
    y = sosfiltfilt(sos, data)
    return y

# Apply the filter to your seismic data
fs = 250  # Sampling frequency in Hz
lowcut = 10  # Low frequency to pass (Hz)
highcut = 50  # High frequency to pass (Hz)

# Assuming your seismic traces are columns in the dataframe
filtered_data = seismic_data.copy()
for column in filtered_data.columns:
    # Ensure we're only filtering seismic data, not metadata like source/receiver positions
    if column.startswith('Trace_'):  # Adjust this condition based on your column names
        filtered_data[column] = butter_bandpass_filter(filtered_data[column], lowcut, highcut, fs, order=6)

filtered_data.to_csv('2d_seismic_date_filtered_data.csv', index=False)
