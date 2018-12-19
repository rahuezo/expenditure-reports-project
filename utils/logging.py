import csv, os

ERROR_LOG = "errors.csv"


def setup_error_log(p=None): 
    fpath = ERROR_LOG if not p else p
    if not os.path.exists(fpath): 
        with open(fpath, "wb") as errors_csv: 
            writer = csv.writer(errors_csv)
            writer.writerow(["File", "Error"])
    return fpath

def log_error(f, e): 
    fpath = setup_error_log()

    with open(fpath, "ab") as errors_csv: 
        writer = csv.writer(errors_csv)
        writer.writerow([f, str(e)])