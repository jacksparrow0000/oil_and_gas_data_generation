import pandas as pd

# Load the seismic data
df = pd.read_csv('synthetic_2d_seismic_for_geometry_correction.csv')

# Example correction: Assuming there's a known offset to be corrected
known_offset_x = 5  # Example offset in meters
df['corrected_source_x'] = df['Source_X'] + known_offset_x
df['corrected_receiver_x'] = df['Receiver_X'] + known_offset_x

# Save the corrected data back to CSV
df.to_csv('synthetic_2d_seismic_corrected_data.csv', index=False)
