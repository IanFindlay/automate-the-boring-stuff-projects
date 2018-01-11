#!/usr/bin/env python3

"""Finds and decrpyts all encrypted PDF files in the folder tree starting from the CWD.

Usage:
pdf_paranoia takes one argument - the password to decrypt the PDF's with.
"""

import os
import sys
import PyPDF2

password = sys.argv[1]
decrypt_failed = []

for folders, subfolders, filenames in os.walk('.'):

    for filename in filenames:
        if filename.endswith('.pdf'):
            path = os.path.join(folders, filename)
            pdf_reader = PyPDF2.PdfFileReader(open(path, 'rb'))
            if pdf_reader.isEncrypted is True:
                if pdf_reader.decrypt(password) != 1:
                    print(filename + ' failed to decrypt.')
                    decrypt_failed.append(filename)
                else:
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))

                    # Encrypt copy of PDF and save with _encrypted suffix
                    decrypted_path = path[:-4] + '_decrpyted.pdf'
                    decrypted_version = open(decrypted_path, 'wb')
                    pdf_writer.write(decrypted_version)
                    decrypted_version.close()

if decrypt_failed != []:
    print("All encrypted PDF's, except those listed above, were "
          "decrypted successfully. All of the original files have been kept.")
else:
    print("All encrypted PDF's in the folder tree were decrypted successfully. "
          "The original files have been kept.")
