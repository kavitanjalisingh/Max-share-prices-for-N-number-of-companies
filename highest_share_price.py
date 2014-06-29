import pandas


def HighestShareForCompany(file_path):
    """
    Returns list for each Company year and month in which the share price \
    was highest.

    :param file_path: CSV file path to be used.

    Usage:
    >>> from <file_name> import HighestShareForCompany
    >>> HighestShareForCompany('test.csv')
    """
    datafile = pandas.read_csv(file_path)
    columns = datafile.columns
    final_list = []
    for i in range(len(columns)):
        dict = {}
        header = datafile.columns[i]
        if header == 'Year' or header == 'Month':
            pass
        else:
            var = zip(datafile.Year, datafile.Month, datafile[header])
            max_value = max(datafile[header])
            max_indices = [i for i, j in enumerate(datafile[header]) \
                            if j==max_value]
            if len(max_indices) > 1:
                dict[header] = []
                for i in max_indices:
                    dict[header].append(var[i])
            else:
                max_index = datafile[header].argmax()
                comp_max_share = var[max_index]
                dict[header] = comp_max_share
            final_list.append(dict)

    return final_list
