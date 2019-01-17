"""
Usage: get_data.py --year=&lt;year&gt;
"""
import requests
import os
from docopt import docopt

# docopt helps parsing the command line argument in
# a simple manner (http://docopt.org/)
args = docopt(doc=__doc__, argv=None,
help=True, version=None,
options_first=False)

year = args['--year']

# Create directory if not present
year_directory_name = 'data/{year}'.format(year=year)
if not os.path.exists(year_directory_name):
    os.makedirs(year_directory_name)

# Fetching file list for the corresponding year
year_data_files = requests.get(
'http://data.pystock.com/{year}/index.txt'.format(year=year)
).text.strip().split('\n')

for data_file_name in year_data_files:
    file_location = '{year_directory_name}/{data_file_name}'.format(
year_directory_name=year_directory_name,
data_file_name=data_file_name)

with open(file_location, 'wb+') as data_file:
    print('&gt;&gt;&gt; Downloading \t {file_location}'.format(file_location=file_location))
    data_file_content = requests.get(
'http://data.pystock.com/{year}/{data_file_name}'.format(year=year, data_file_name=data_file_name)
        ).content
    print('&lt;&lt;&lt; Download Completed \t {file_location}'.format(file_location=file_location))
    data_file.write(data_file_content)
