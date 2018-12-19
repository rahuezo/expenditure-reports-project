from utils.convert import pdf_to_csv
from utils.logging import log_error

import tkFileDialog as fd


def main(): 
    pdfs = sorted(fd.askopenfilenames(title="Choose expenditure reports"), reverse=True)

    for pdf in pdfs:
		# try:
		pdf_to_csv(pdf)
		# except Exception as e: 
			# log_error(pdf, e)
			# continue            

main()