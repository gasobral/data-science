import zipfile
from pathlib import Path


## Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def data_aquisition(data_path : dict) -> None:
    """
    Retreives the data from raw directory (under
    <project root>/data/raw) and extract them to processed directory.

    Arguments
    ---------
        data_path: a dictionary containing the path structure of the
                   data directories.
    Return
    ------
        None
    """

    for curr_file in data_path['raw'].glob('*.zip'):
        with zipfile.ZipFile(curr_file, 'r') as zip_ref:
            print(f'Decompressing the file {curr_file}')
            zip_ref.extractall(data_path['processed'])
            print(f'Decompressed the file at {data_path["processed"]}')


## Code to test data aquisition functions - - - - - - - - - - - - - -#
if __name__ == "__main__":
    ## loads the data directory structure
    from config import data_path

    print('Testing the implementation of function: data_aquisition',
          end='\n\n')
    data_aquisition(data_path)
