import numpy as np


def __single_table_print(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best, use_max_good_idx, n_dec:int):
    n_Regions = len(Region_labels)
    n_Metrics = len(Metric_labels)
    n_Cases = len(Case_labels)
    if Case_Abr is None:
        Case_Abr = Case_labels

    table_head = "\\begin{tabular}{|c|"
    data_col_type = "S[table-format=2." + str(n_dec) + ", round-precision= " + str(n_dec) + ", round-mode=places] "
    for i in range(n_Metrics):
        for j in range(n_Cases):
            table_head += data_col_type
        table_head += "| "
    table_head += "}\n"

    table_super_labels = "\\hline\n\\text{Region} "
    for i in range(n_Metrics):
        table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{\\text{{" + Metric_labels[i] + "}} "
    table_super_labels += "\\\\ \\hline\n"

    table_sub_labels = "\\text{Case:} "
    for i in range(n_Metrics):
        for j in range(n_Cases):
            table_sub_labels += "& \\text{" + Case_Abr[j] + "} "
    table_sub_labels += "\\\\ \\hline\n"

    table_data = ""

    if highlight_best == False:
        for i in range(n_Regions):
            a_row = "\\text{" + Region_labels[i] + "} "
            for j in range(n_Metrics):
                for k in range(n_Cases):
                    a_row += "& " + str(Data[i,j,k]) + " "
            a_row += " \\\\ \\hline\n"
            table_data += a_row
    else:
        for i in range(n_Regions):
            a_row = "\\text{" + Region_labels[i] + "} "
            for j in range(n_Metrics):
                if j in use_max_good_idx:
                    best_k_idx = np.nanargmax(Data[i, j])
                else:
                    best_k_idx = np.nanargmin(Data[i, j])
                for k in range(n_Cases):
                    if k != best_k_idx:
                        a_row += "& " + str(Data[i, j, k]) + " "
                    else:
                        a_row += "& \\cellcolor[HTML]{34FF34} " + str(Data[i, j, k]) + " "
            a_row += " \\\\ \\hline\n"
            table_data += a_row


    full_table = table_head + table_super_labels + table_sub_labels + table_data + "\\end{tabular}\n"
    return full_table


def __single_table_print_v2(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best, use_max_good_idx, n_dec:int):
    n_Regions = len(Region_labels)
    n_Metrics = len(Metric_labels)
    n_Cases = len(Case_labels)
    if Case_Abr is None:
        Case_Abr = Case_labels

    table_head = "\\begin{tabular}{|c|"
    data_col_type = "c "
    for i in range(n_Metrics):
        for j in range(n_Cases):
            table_head += data_col_type
        table_head += "| "
    table_head += "}\n"

    table_super_labels = "\\hline\n\\text{Region} "
    for i in range(n_Metrics):
        table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{\\text{{" + Metric_labels[i] + "}} "
    table_super_labels += "\\\\ \\hline\n"

    table_sub_labels = "\\text{Case:} "
    for i in range(n_Metrics):
        for j in range(n_Cases):
            table_sub_labels += "& \\text{" + Case_Abr[j] + "} "
    table_sub_labels += "\\\\ \\hline\n"

    table_data = ""

    if highlight_best == False:
        for i in range(n_Regions):
            a_row = "\\text{" + Region_labels[i] + "} "
            for j in range(n_Metrics):
                for k in range(n_Cases):
                    a_row += "& " + ("{:." + str(n_dec) + "f}").format(Data[i,j,k]) + " "
            a_row += " \\\\ \\hline\n"
            table_data += a_row
    else:
        for i in range(n_Regions):
            a_row = "\\text{" + Region_labels[i] + "} "
            for j in range(n_Metrics):
                # if j in use_max_good_idx:
                max_k = np.nanmax(Data[i, j])
                min_k = np.nanmin(Data[i, j])
                for k in range(n_Cases):
                    score = (Data[i,j,k] - min_k)/(max_k-min_k)*360
                    print(score, Data[i,j], min_k, max_k)
                    if j not in use_max_good_idx:
                        score = 360 - score
                    if score == score:
                        score = str(int(score))
                        a_row += "&  " + ("{:." + str(n_dec) + "f}").format(Data[i,j,k]) + " \\priority{" + score + "} "
                    else:
                        a_row += "&  " + ("{:." + str(n_dec) + "f}").format(
                            Data[i, j, k]) + " "
            a_row += " \\\\ \\hline\n"
            table_data += a_row


    full_table = table_head + table_super_labels + table_sub_labels + table_data + "\\end{tabular}\n"
    return full_table





def __multi_table_print(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best, use_max_good_idx, n_dec:int, metrics_per_table):
    n_Regions = len(Region_labels)
    n_Metrics = len(Metric_labels)
    n_Cases = len(Case_labels)
    if Case_Abr is None:
        Case_Abr = Case_labels

    table_head = "\\begin{tabular}{c "
    data_col_type = "S[table-format=2." + str(n_dec) + ", round-precision= " + str(n_dec) + ", round-mode=places] "
    for i in range(metrics_per_table):
        for j in range(n_Cases):
            table_head += data_col_type
    table_head += "}\n"

    if highlight_best:
        col_head = "\\cellcolor[HTML]{34FF34}"
    else:
        col_head = ""

    Count = 0
    table_body = ""
    while Count < n_Metrics:
        Count += metrics_per_table

        if Count < n_Metrics:
            table_super_labels = "\\hline\n\\multicolumn{1}{|c|}{\\text{Region}} "
            for i in range(metrics_per_table):
                table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{\\text{{" + Metric_labels[Count - metrics_per_table + i] + "}} "
            table_super_labels += "\\\\ \\hline\n"
            table_sub_labels = "\\multicolumn{1}{|c|}{\\text{Cases:}}"
            for i in range(metrics_per_table):
                for j in range(n_Cases):
                    if j == n_Cases - 1:
                        table_sub_labels += "& \\multicolumn{1}{c|}{\\text{" + Case_Abr[j] + "}} "
                    else:
                        table_sub_labels += "& \\multicolumn{1}{c}{\\text{" + Case_Abr[j] + "}} "

            table_sub_labels += "\\\\ \\hline\n"
            all_rows = ""
            for i in range(n_Regions):
                a_row = "\\multicolumn{1}{|c|}{\\text{" + Region_labels[i] + "}} "
                for j in range(metrics_per_table):
                    if j  + Count - metrics_per_table in use_max_good_idx:
                        best_k_idx = np.nanargmax(Data[i, Count - metrics_per_table + j])
                    else:
                        best_k_idx = np.nanargmin(Data[i, Count - metrics_per_table + j])
                    for k in range(n_Cases):
                        if k == best_k_idx:
                            temp = col_head + " "
                        else:
                            temp = " "
                        if k == n_Cases - 1:
                            a_row += "& \\multicolumn{1}{" + data_col_type + "|}{" + temp + str(Data[i, Count - metrics_per_table + j, k]) + "} "
                        else:
                            a_row += "& " + temp + str(Data[i,Count - metrics_per_table + j,k]) + " "
                a_row += " \\\\ \\hline\n"
                all_rows += a_row

            table_break =  ""
            for i in range(metrics_per_table * n_Cases):
                table_break += " &"
            table_break += "\\\\ \n"
            table_body += table_super_labels + table_sub_labels + all_rows + table_break

        else:
            start = Count - metrics_per_table
            n_overflow_metrics = n_Metrics - (Count - metrics_per_table)
            line_case = "\\cline{1-" + str(n_overflow_metrics * n_Cases+1) + "}"
            n_empty_cols = (metrics_per_table - n_overflow_metrics) * n_Cases

            table_super_labels = line_case + "\n\\multicolumn{1}{|c|}{\\text{Region}} "
            for i in range(n_overflow_metrics):
                table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{\\text{{" + Metric_labels[start + i] + "}} "
            for i in range(n_empty_cols):
                table_super_labels += " &"
            table_super_labels += "\\\\ " + line_case + "\n"
            table_sub_labels = "\\multicolumn{1}{|c|}{\\text{Cases:}}"
            for i in range(n_overflow_metrics):
                for j in range(n_Cases):
                    if j == n_Cases - 1:
                        table_sub_labels += "& \\multicolumn{1}{c|}{\\text{" + Case_Abr[j] + "}} "
                    else:
                        table_sub_labels += "& \\multicolumn{1}{c}{\\text{" + Case_Abr[j] + "}} "
            for i in range(n_empty_cols):
                table_sub_labels += " &"
            table_sub_labels += "\\\\ " + line_case + "\n"
            all_rows = ""
            for i in range(n_Regions):
                a_row = "\\multicolumn{1}{|c|}{\\text{" + Region_labels[i] + "}} "
                for j in range(n_overflow_metrics):
                    if j + Count - metrics_per_table in use_max_good_idx:
                        best_k_idx = np.nanargmax(Data[i, Count - metrics_per_table + j])
                    else:
                        best_k_idx = np.nanargmin(Data[i, Count - metrics_per_table + j])
                    for k in range(n_Cases):
                        if k == best_k_idx:
                            temp = col_head + " "
                        else:
                            temp = " "
                        if k == n_Cases - 1:
                            a_row += "& \\multicolumn{1}{" + data_col_type + "|}{" + temp + str(
                                Data[i, start + j, k]) + "} "
                        else:
                            a_row += "& " + temp + str(Data[i, Count - metrics_per_table + j, k]) + " "
                for i in range(n_empty_cols):
                    a_row += " &"
                a_row += " \\\\ " + line_case + "\n"
                all_rows += a_row

            table_body += table_super_labels + table_sub_labels + all_rows



        # else:
        #     for i in range(n_Metrics - (Count - metrics_per_table)):
        #         table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{\\text{{" + Metric_labels[
        #             Count - metrics_per_table + i] + "}} "
        #     for i in range(metrics_per_table - (n_Metrics - (Count - metrics_per_table))):
        #         table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{}} "
        #     table_super_labels += "\\\\ \\hline\n"
        #     table_sub_labels = "None"

        # print(table_super_labels + table_sub_labels)
        # table_body += table_super_labels + table_sub_labels
    # exit()



    # table_sub_labels = "\\text{Case:} "
    # for i in range(n_Metrics):
    #     for j in range(n_Cases):
    #         table_sub_labels += "& \\text{" + Case_Abr[j] + "} "
    # table_sub_labels += "\\\\ \\hline\n"
    #
    # table_data = ""
    #
    # if highlight_best == False:
    #     for i in range(n_Regions):
    #         a_row = "\\text{" + Region_labels[i] + "} "
    #         for j in range(n_Metrics):
    #             for k in range(n_Cases):
    #                 a_row += "& " + str(Data[i,j,k]) + " "
    #         a_row += " \\\\ \\hline\n"
    #         table_data += a_row
    # else:
    #     for i in range(n_Regions):
    #         a_row = "\\text{" + Region_labels[i] + "} "
    #         for j in range(n_Metrics):
    #             if j in use_max_good_idx:
    #                 best_k_idx = np.nanargmax(Data[i, j])
    #             else:
    #                 best_k_idx = np.nanargmin(Data[i, j])
    #             for k in range(n_Cases):
    #                 if k != best_k_idx:
    #                     a_row += "& " + str(Data[i, j, k]) + " "
    #                 else:
    #                     a_row += "& \\cellcolor[HTML]{34FF34} " + str(Data[i, j, k]) + " "
    #         a_row += " \\\\ \\hline\n"
    #         table_data += a_row


    full_table = table_head + table_body + "\\end{tabular}\n"
    return full_table

def __multi_table_print_v2(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best, use_max_good_idx, n_dec:int, metrics_per_table):
    n_Regions = len(Region_labels)
    n_Metrics = len(Metric_labels)
    n_Cases = len(Case_labels)
    if Case_Abr is None:
        Case_Abr = Case_labels

    table_head = "\\begin{tabular}{c "
    data_col_type = "c "
    for i in range(metrics_per_table):
        for j in range(n_Cases):
            table_head += data_col_type
    table_head += "}\n"

    Count = 0
    table_body = ""
    while Count < n_Metrics:
        Count += metrics_per_table

        if Count < n_Metrics:
            table_super_labels = "\\hline\n\\multicolumn{1}{|c|}{\\text{Region}} "
            for i in range(metrics_per_table):
                table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{\\text{{" + Metric_labels[Count - metrics_per_table + i] + "}} "
            table_super_labels += "\\\\ \\hline\n"
            table_sub_labels = "\\multicolumn{1}{|c|}{\\text{Cases:}}"
            for i in range(metrics_per_table):
                for j in range(n_Cases):
                    if j == n_Cases - 1:
                        table_sub_labels += "& \\multicolumn{1}{c|}{\\text{" + Case_Abr[j] + "}} "
                    else:
                        table_sub_labels += "& \\multicolumn{1}{c}{\\text{" + Case_Abr[j] + "}} "

            table_sub_labels += "\\\\ \\hline\n"
            all_rows = ""
            for i in range(n_Regions):
                a_row = "\\multicolumn{1}{|c|}{\\text{" + Region_labels[i] + "}} "
                for j in range(metrics_per_table):
                    for k in range(n_Cases):
                        max_k = np.nanmax(Data[i, Count - metrics_per_table + j])
                        min_k = np.nanmin(Data[i, Count - metrics_per_table + j])
                        score = (Data[i, Count - metrics_per_table + j, k] - min_k) / (max_k - min_k) * 360
                        if j not in use_max_good_idx:
                            score = 360 - score
                        if highlight_best and score == score:
                            temp = " \\priority{" + str(int(score)) + "} "
                        else:
                            temp = ""

                        Data_str = ("{:." + str(n_dec) + "f}").format(Data[i, Count - metrics_per_table + j, k])
                        if k == n_Cases - 1:
                            a_row += "& \\multicolumn{1}{" + data_col_type + "|}{" + Data_str + temp + "} "
                        else:
                            a_row += "& " + Data_str + temp + " "
                a_row += " \\\\ \\hline\n"
                all_rows += a_row

            table_break =  ""
            for i in range(metrics_per_table * n_Cases):
                table_break += " &"
            table_break += "\\\\ \n"
            table_body += table_super_labels + table_sub_labels + all_rows + table_break

        else:
            start = Count - metrics_per_table
            n_overflow_metrics = n_Metrics - (Count - metrics_per_table)
            line_case = "\\cline{1-" + str(n_overflow_metrics * n_Cases+1) + "}"
            n_empty_cols = (metrics_per_table - n_overflow_metrics) * n_Cases

            table_super_labels = line_case + "\n\\multicolumn{1}{|c|}{\\text{Region}} "
            for i in range(n_overflow_metrics):
                table_super_labels += f"& \\multicolumn{{{n_Cases}}}{{c|}}{{\\text{{" + Metric_labels[start + i] + "}} "
            for i in range(n_empty_cols):
                table_super_labels += " &"
            table_super_labels += "\\\\ " + line_case + "\n"
            table_sub_labels = "\\multicolumn{1}{|c|}{\\text{Cases:}}"
            for i in range(n_overflow_metrics):
                for j in range(n_Cases):
                    if j == n_Cases - 1:
                        table_sub_labels += "& \\multicolumn{1}{c|}{\\text{" + Case_Abr[j] + "}} "
                    else:
                        table_sub_labels += "& \\multicolumn{1}{c}{\\text{" + Case_Abr[j] + "}} "
            for i in range(n_empty_cols):
                table_sub_labels += " &"
            table_sub_labels += "\\\\ " + line_case + "\n"
            all_rows = ""
            for i in range(n_Regions):
                a_row = "\\multicolumn{1}{|c|}{\\text{" + Region_labels[i] + "}} "
                for j in range(n_overflow_metrics):
                    for k in range(n_Cases):
                        if k == n_Cases - 1:
                            max_k = np.nanmax(Data[i, start + j])
                            min_k = np.nanmin(Data[i, start + j])

                            score = (Data[i, start + j, k] - min_k) / (max_k - min_k) * 360
                            if start + j not in use_max_good_idx:
                                score = 360 - score
                        else:
                            max_k = np.nanmax(Data[i, Count - metrics_per_table + j])
                            min_k = np.nanmin(Data[i, Count - metrics_per_table + j])

                            score = (Data[i, Count - metrics_per_table + j, k] - min_k) / (max_k - min_k) * 360
                            if Count - metrics_per_table + j not in use_max_good_idx:
                                score = 360 - score

                        if highlight_best and score == score:
                            temp = " \\priority{" + str(int(score)) + "} "
                        else:
                            temp = ""

                        if k == n_Cases - 1:
                            Data_str = ("{:." + str(n_dec) + "f}").format(Data[i, start + j, k])
                            a_row += "& \\multicolumn{1}{" + data_col_type + "|}{" + Data_str + temp + "} "
                        else:
                            Data_str = ("{:." + str(n_dec) + "f}").format(Data[i, Count - metrics_per_table + j, k])
                            a_row += "& " + Data_str + temp + " "
                for i in range(n_empty_cols):
                    a_row += " &"
                a_row += " \\\\ " + line_case + "\n"
                all_rows += a_row

            table_body += table_super_labels + table_sub_labels + all_rows


    full_table = table_head + table_body + "\\end{tabular}\n"
    return full_table

def Region_Case_Metric_table_Build(Data:np.ndarray, Region_labels:list, Metric_labels:list, Case_labels:list, Case_Abr = None, table_title = None, table_caption = None, highlight_best = True, use_max_good_idx = (), metrics_per_table = -1, n_dec = 3, include_table_abr_defs = True):
    ans = "\\begin{table*}[!htb]\n\\centering\n"
    if table_title is not None or table_caption is not None or (include_table_abr_defs and Case_Abr is not None):
        ans += "\\caption{"
        if table_title is not None:
            ans += "\\label{Tab:" + table_title + "}"
        if table_caption is not None:
            ans += table_caption
        if (include_table_abr_defs and Case_Abr is not None):
            for i in range(len(Case_labels)):
                ans += " Case " + Case_Abr[i] + ": " + Case_labels[i] + "."
        ans += "}\n"

    if metrics_per_table < 1:
        ans += __single_table_print(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best, use_max_good_idx, n_dec)
    else:
        ans += __multi_table_print(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best,
                                    use_max_good_idx, n_dec, metrics_per_table)

    ans += "\\end{table*}\n"
    return ans

def Region_Case_Metric_table_Build_v2(Data:np.ndarray, Region_labels:list, Metric_labels:list, Case_labels:list, Case_Abr = None, table_title = None, table_caption = None, highlight_best = True, use_max_good_idx = (), metrics_per_table = -1, n_dec = 3, include_table_abr_defs = True):
    ans = "\\begin{table*}[!htb]\n\\centering\n"
    if table_title is not None or table_caption is not None or (include_table_abr_defs and Case_Abr is not None):
        ans += "\\caption{"
        if table_title is not None:
            ans += "\\label{Tab:" + table_title + "}"
        if table_caption is not None:
            ans += table_caption
        if (include_table_abr_defs and Case_Abr is not None):
            for i in range(len(Case_labels)):
                ans += " Case " + Case_Abr[i] + ": " + Case_labels[i] + "."
        ans += "}\n"

    if metrics_per_table < 1:
        ans += __single_table_print_v2(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best, use_max_good_idx, n_dec)
    else:
        ans += __multi_table_print_v2(Data, Region_labels, Metric_labels, Case_labels, Case_Abr, highlight_best,
                                    use_max_good_idx, n_dec, metrics_per_table)

    ans += "\\end{table*}\n"
    return ans
