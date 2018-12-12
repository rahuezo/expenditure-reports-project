from tabula import read_pdf
import tkFileDialog as fd

COLUMNS = [77, 164, 207, 414, 466, 560, 655, 767, 871, 983]

def pdf_to_csv(f, outf=None): 
    df = read_pdf(f, lattice=True, columns=COLUMNS)
    df.to_csv("{}.csv".format(f) if not outf else outf)


f = fd.askopenfilename(title="Choose pdf for pdf_to_csv")

pdf_to_csv(f)