import mg_table_2_latex
import numpy as np
import argparse

def  example_for_3D_data():
    """
    This function creates a small example table
    :return:
    String for LaTeX table
    """

    Datasets = ["2000", "2001", "2002", "2003", "2004"]
    Cases = ["Factory 1", "Factory 2", "Factory 3"]
    Metrics = ["Average Working Widgets made per Day $\\uparrow$", "Cost per Widget $\\downarrow$",
               "Percent faulty Widgets $\\downarrow$", "Cost to Ship $\\downarrow$"]
    max_good = (0,)
    Abr = ["F1", "F2", "F3"]
    Caption = "Example of a table produced by mg\\_Table\\_builder showing properties of three factories producing widgets over five years."
    title = "Example_Table"
    # Abr = ["AWWpD", "CpW", "\\%PfW", "C2S"] #Abrs for Metrics

    #Generate Random data to be saved
    Data = 100*np.random.rand(len(Datasets) * len(Metrics) * len(Cases)).reshape([len(Datasets), len(Metrics), len(Cases)])
    table_str = mg_table_2_latex.Multi_data_Multi_test_Table(Data, Datasets, Metrics, Cases, metrics_per_table=2, Case_Abr=Abr,
                                                       n_dec=2, table_caption=Caption, table_title=title, use_max_good_idx=max_good)

    return table_str

def color_example():
    """
    This creates a small table showing how the color indicators work.
    :return:
    String for LaTeX table
    """
    Datasets = ["Angle", "Shifted Angle"]
    Cases = ["Best", "75\\%", "50\\%", "25\\%", "Worst"]
    Metrics = ["Amount Green $\\uparrow$"]
    max_good = (0,)
    Caption = "Example of how colored indicators work."
    title = "Example_Table_for_Colors"

    Data = np.zeros([len(Datasets), len(Metrics), len(Cases)])
    Data[0, 0] = [360, 270, 180, 90, 0]
    Data[1, 0] = Data[0, 0] + 180
    table_str = mg_table_2_latex.Multi_data_Multi_test_Table(Data, Datasets, Metrics, Cases,
                                                             n_dec=0, table_caption=Caption, table_title=title,
                                                             use_max_good_idx=max_good)
    return table_str

def make_example_tex_file():
    """
    Creates a string that can be saved to as a .tex file and shows some example tables.
    :return:
    String to be saved as .tex file
    """
    out_str = "\\documentclass{article}\n\\usepackage[margin=1.in]{geometry}\n\n"

    #Get required packages
    out_str += mg_table_2_latex.get_LaTeX_packages()

    out_str += "\n\n\\title{Example Tables}\n"
    out_str += "\\begin{document}\n"
    out_str += "\\maketitle\n\n"

    out_str += "This document provides examples of a table the mg\\_table\\_2\\_latex program can generate.\n"
    out_str += "Table \\ref{Tab:Example_Table} contains data representing the performance of three factories producing widgets.\n"
    out_str += "Table \\ref{Tab:Example_Table_for_Colors} shows how indicators are used.\n\n"
    out_str += example_for_3D_data()
    out_str += "\n\n"
    out_str += color_example()
    out_str += "\n\n"


    out_str += "\\end{document}"

    return out_str


if __name__ == '__main__':
    #Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", type=str, required=True, help="Name of output file for example.")
    args = parser.parse_args()
    out_file = args.file_name

    #Ensure a .tex file is created
    if len(out_file) < 4  or out_file[-4::] != ".tex":
        out_file += ".tex"
    print("Creating example .tex file:", out_file)

    #Save File
    fout = open(out_file, "w")
    fout.write(make_example_tex_file())
    fout.close()
    print("Done")