from PyPDF2 import PdfMerger
import os

pdfs = sorted([f for f in os.listdir("pdfs") if f.endswith(".pdf")])

merger = PdfMerger()
for pdf in pdfs:
    merger.append(os.path.join("pdfs", pdf))

merger.write("merged.pdf")
merger.close()

print("All PDFs merged into merged.pdf")
