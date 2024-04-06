import pandas as pd 
import numpy as np 
import chardet


# Replace 'your_file.csv' with the path to your CSV file
with open('data/spotify-2023.csv', 'rb') as f:
    result = chardet.detect(f.read())  # Detect the encoding

