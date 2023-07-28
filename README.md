# Data 2 Tables

## Purpose
This code takes a numpy array of floats and creates a string that can be copied directly into LaTeX as a table.
The code automatically rounds and places indicators by results, showing how good the results are relative to other values in the table.
See Example.pdf for an example of the output tables.

## Setup

This code uses numpy and argparse.
Argparse is not used outside of main_Example.

To create an example .tex file, run
``
python main_Example.py --file_name FILE_NAME
``

## Usage
This code contains two functions in mg_table_2_latex

1) ```Python
   get_LaTeX_packages() -> str:
    """
    Get packages needed for LaTeX
    :return:
    A string to copy into the LaTeX file
    """
   ```
2) ```Python
   Multi_data_Multi_test_Table(Data:np.ndarray, Dataset_labels:list, Metric_labels:list, Case_labels:list,
                                      Case_Abr = None, table_title = None, table_caption = None, highlight_best = True,
                                      use_max_good_idx = (), metrics_per_table = -1, n_dec = 3,
                                      include_table_abr_defs = True, add_average = True, placement_indicators = "[h]") -> str:
    """
    This function automatically takes a 3D tensor and creates LaTeX table that rounds and colors the data.
    It returns a string that can be copied into LaTeX

    Args:
       Data: A x B x C array of floats, where A,B,C > 0
       Dataset_labels:  List of strings with length of A, containing names of the datasets in Data
       Metric_labels: List of strings with length of B, containing names of metrics
       Case_labels: List of strings with length of C, containing names of cases

    Optional Args:
       Case_Abr: List of strings of length of C of abbreviated case names, default = None
       table_title: str that will appear as \label{Tab:str}, ignored if set to None, default = None
       table_caption: Caption for table, default = None
       highlight_best: Place circle indicators indicated score performance, default = True
       use_max_good_idx: List of integers in [0, B-1] indicating metrics where large scores indicate good results, default = ()
       metrics_per_table: Number of metrics to be placed on a single, negative numbers indicate to only use a single table, default = -1
       n_dec: Number of points past the decimal point to disply, default = 3
       include_table_abr_defs: Use Case_Abr if available, default = True
       add_average: Adds average of cases to data, default = True
       placement_indicators: str that controls the placement of the table in document, i.e. [], [!h], [th] ect, default: [h]

    Returns:
        str of code that can be copied into LaTeX

    """
   ```
