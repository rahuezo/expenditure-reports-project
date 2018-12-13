from tabula import read_pdf

import tkFileDialog as fd
import numpy as np
import csv

COLUMNS = [77, 164, 207, 414, 466, 560, 655, 767, 871, 983]


def write_to_csv(f, rows): 
    print "\nWriting {} rows to {}\n".format(len(rows), f)

    with open(f, "wb") as out_csv: 
        writer = csv.writer(out_csv, delimiter=",")
        writer.writerows(rows)

    print "\tFinished!\n"

def get_average_columns(rows): 
    if not len(rows) > 0: 
        return -1
    return sum(map(lambda x: len(x), rows)) / float(len(rows))

def pdf_to_csv(f, outf=None): 
    rows_container = []
    page_count = 0 

    while True: 
        try: 
            df = read_pdf(f, lattice=True, columns=COLUMNS, pages=page_count) # Only get ith page in pdf
            df = df.replace(np.nan, "", regex=True)

            if page_count == 0: 
                rows_container.append(list(df)) # Write header to rows_container

            rows_container.extend(df.values.tolist())
            page_count += 1
        except: 
            break
    
    print "Page Count: {}".format(page_count)

    avg_columns = get_average_columns(rows_container)

    if not avg_columns.is_integer(): 
        raise Exception("Number of columns is not consistent among pages!")

    print "\nAvg. Columns: {}\n".format(avg_columns)

    output_filename = "{}.csv".format(f) if not outf else outf
    
    write_to_csv(output_filename, rows_container)

f = fd.askopenfilename(title="Choose pdf for pdf_to_csv")

pdf_to_csv(f)