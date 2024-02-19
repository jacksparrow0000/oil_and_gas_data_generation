import numpy as np
import pandas as pd

# Parameters
num_traces = 100
sampling_rate = 500  # Hz
duration = 2  # seconds
source_start_x = 0  # meters
receiver_start_x = 10  # meters
spacing = 10  # meters between each source-receiver pair

# Simulate seismic wavelet (Ricker wavelet)
def ricker_wavelet(freq, length, dt):
    t = np.arange(-length / 2, (length / 2) + dt, dt)
    y = (1.0 - 2.0 * (np.pi ** 2) * (freq ** 2) * (t ** 2)) * np.exp(-(np.pi ** 2) * (freq ** 2) * (t ** 2))
    return y

# Generate synthetic seismic traces
def generate_traces(num_traces, sampling_rate, duration):
    dt = 1 / sampling_rate
    time = np.arange(0, duration, dt)
    freq = 25  # Frequency of the Ricker wavelet
    wavelet = ricker_wavelet(freq, duration, dt)
    traces = np.array([np.convolve(np.random.randn(len(time)), wavelet, mode='same') for _ in range(num_traces)])
    return traces

# Generate source and receiver positions
def generate_positions(num_traces, source_start_x, receiver_start_x, spacing):
    source_x = np.arange(source_start_x, source_start_x + num_traces * spacing, spacing)
    receiver_x = np.arange(receiver_start_x, receiver_start_x + num_traces * spacing, spacing)
    return source_x, receiver_x

# Create the dataset
traces = generate_traces(num_traces, sampling_rate, duration)
source_x, receiver_x = generate_positions(num_traces, source_start_x, receiver_start_x, spacing)

# Adjusting the DataFrame creation
# Now, each trace is a row in the DataFrame, and we add source_x and receiver_x as columns
df = pd.DataFrame(traces)
df['Source_X'] = pd.Series(source_x)
df['Receiver_X'] = pd.Series(receiver_x)

# Save to CSV file
df.to_csv('synthetic_2d_seismic_for_geometry_correction.csv', index=False)
