#!/usr/bin/env python3

"""Finds and encrypts all unencrypted PDF's in a folder tree starting from the CWD.

Usage:
pdf_paranoia takes one argument - the password to encrypt the PDF's with.
"""

import os
import sys
import PyPDF2

password = sys.argv[1]
encrypt_failed = []

for folders, subfolders, filenames in os.walk('.'):

    for filename in filenames:
        if filename.endswith('.pdf'):
            path = os.path.join(folders, filename)
            pdf_reader = PyPDF2.PdfFileReader(open(path, 'rb'))
            if pdf_reader.isEncrypted is False:
                pdf_writer = PyPDF2.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

                # Encrypt copy of PDF and save with _encrypted suffix
                pdf_writer.encrypt(password)
                encrypted_path = path[:-4] + '_encrpyted.pdf'
                encrypted_version = open(encrypted_path, 'wb')
                pdf_writer.write(encrypted_version)
                encrypted_version.close()

                # Check file was encrypted properly
                pdf_reader = PyPDF2.PdfFileReader(open(encrypted_path, 'rb'))
                if (pdf_reader.isEncrypted is True
                        and pdf_reader.decrypt(password) == 1):
                    os.remove(path)
                else:
                    encrypt_failed.append(filename)

if encrypt_failed != []:
    print('The following files failed their encryption checks and were '
          'not deleted:')
    for filename in encrypt_failed:
        print(filename)
else:
    print("All PDF's files in the folder tree have been encrypted successfully. "
          "The original files have been deleted.")
