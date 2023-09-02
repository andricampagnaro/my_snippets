import pandas as pd
import numpy as np

# Define the number of rows in the dataset
num_rows = 10000000

# Generate a random longitude for each row
pickup_longitude = np.random.uniform(low=-38.0, high=-94.0, size=num_rows)

# Generate a random trip duration for each row
trip_duration = np.random.normal(loc=10, scale=5, size=num_rows)

# Create a DataFrame with the pickup longitude and trip duration columns
df = pd.DataFrame(
    {"pickup_longitude": pickup_longitude, "trip_duration": trip_duration}
)

#

import duckdb

def find_avg_trip_duration_in_the_west():
    return duckdb.execute(
        'SELECT AVG(trip_duration) FROM df WHERE pickup_longitude < -73.95'
    ).df()