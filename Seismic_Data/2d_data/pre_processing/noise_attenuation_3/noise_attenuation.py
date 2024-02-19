import pandas as pd

# Load the seismic data
csv_file_path = 'path_to_filtered_data.csv'  # Update this path
seismic_data = pd.read_csv(csv_file_path)

from scipy.signal import medfilt

# Assuming each column in your DataFrame represents a seismic trace, except for metadata columns
for column in seismic_data.columns:
    # Adjust this condition based on your DataFrame structure to skip non-seismic data columns
    if column not in ['Source_X', 'Receiver_X']:  # Example to skip source and receiver position columns
        seismic_data[column] = medfilt(seismic_data[column], kernel_size=5)

seismic_data.to_csv('noise_attenuated_seismic_data.csv', index=False)

