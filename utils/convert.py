from tabula import read_pdf
from aesthetics import fix_rows
from logging import log_error

import numpy as np
import csv
import unicodecsv as ucsv


def write_to_csv(f, rows): 
    print "\nWriting {} rows to {}\n".format(len(rows), f)


    with open(f, "wb") as out_csv: 
        writer = ucsv.writer(out_csv, delimiter=",")
        writer.writerows(rows)


    print "\tFinished!\n"

def get_average_columns(rows): 
    print "\t\nGetting average columns"
    if not len(rows) > 0: 
        return -1
    return sum(map(lambda x: len(x), rows)) / float(len(rows))

def pdf_to_csv(f, outf=None): 
    rows_container = []
    page_count = 1 

    print "\nProcessing {}\n\n".format(f)

    while True: 
        try: 
            df = read_pdf(f, lattice=True, pages=page_count) # Only get ith page in pdf
            df = df.replace(np.nan, "", regex=True)

            if page_count == 1: 
                rows_container.append(list(df)) # Write header to rows_container

            rows_container.extend(df.values.tolist())
            page_count += 1
        except Exception as e: 
            break
    
    if df is None: 
        raise Exception("Table couldn't be extracted from {}".format(f))

    print "\tPage Count: {}".format(page_count)

    avg_columns = get_average_columns(rows_container)

    if not avg_columns.is_integer(): 
        log_error(f, "Number of columns is not consistent among pages!")

    #     raise Exception("Number of columns is not consistent among pages!")

    print "\n\tAvg. Columns: {}".format(avg_columns)

    output_filename = "{}.csv".format(f) if not outf else outf
    
    write_to_csv(output_filename, fix_rows(rows_container))

    print "-" * 100