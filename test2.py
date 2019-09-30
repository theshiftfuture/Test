import string as str
import decimal
import numpy as np
import zipfile
s = 'The quick brown fox'
print(str.capwords(s))

fmt = '{0:<25} {1:<25}'
print(fmt.format('Input', 'Output'))



for filename in ['README.txt', 'example.zip', 'bad_example.zip', 'notthere.zip']:
    print('{:>15}  {}'.format(filename, zipfile.is_zipfile(filename)))
