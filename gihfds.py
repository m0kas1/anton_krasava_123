import zipfile
a = 'yyy'

file_zip = zipfile.ZipFile(f'zip/{a}.zip', 'w')
file_zip.close()

file_zip = zipfile.ZipFile(f'zip/{a}.zip', 'a')
file_zip.write('txt/gey.txt')
file_zip.close()