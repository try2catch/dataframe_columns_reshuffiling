# Header Checker

This is a Python script that checks if a given list of headers is valid for a CSV file. It checks if the headers match the indexes given in the list of dictionaries. If the indexes are valid, it creates a new CSV file with the specified headers.

## Prerequisites

- Python 3.x
- Pandas library

## Installation

- Clone the repository: `git clone https://github.com/try2catch/dataframe_columns_reshuffiling.git`
- Install the required libraries: `pip install -r requirements.txt`

## Usage

1. Define the headers with their corresponding indexes in a list of dictionaries.
2. Use the `get_headers()` function to check if the headers are valid for the CSV file and get the list of headers to be used.
3. Read the CSV file using Pandas and select only the columns with the required headers.
4. Save the new CSV file using Pandas.

### Example

```python
import pandas as pd

from header_checker import get_headers

header = [
    {
        "index": 1,
        "name": "country"
    },
    {
        "index": 0,
        "name": "beer_servings"
    },
    {
        "index": 2,
        "name": "spirit_servings"
    },
    {
        "index": 3,
        "name": "wine_servings"
    },
    {
        "index": 4,
        "name": "total_litres_of_pure_alcohol"
    },
    {
        "index": 5,
        "name": "continent"
    }
]

# Check if headers are valid and get the list of headers to be used
required_headers = get_headers(header)

# Read the CSV file and select only the columns with the required headers
df = pd.read_csv('files/drinks.csv')
dff = df[required_headers]

# Save the new CSV file
dff.to_csv('files/output.csv', index=False)

# License
This project is licensed under the MIT License.
