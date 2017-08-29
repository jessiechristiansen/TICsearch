# -*- coding: utf-8 -*-
"""
Spyder Editor
Jessie Christiansen
Aug 28 2017

"""

import astropy
import unicodedata
from astroquery.simbad import Simbad

inputFile = '~/nexsci/fulllist.txt'
outputFile = '~/nexsci/fulllist_with_coords.txt'

lines = [line.rstrip('\n') for line in open(inputFile)]

f = open(outputFile,'w')      


for i in range(len(lines)):

    thisName = lines[i]
    result_table = Simbad.query_object(thisName)

    if result_table is not None:
        ra_a = result_table.columns[1]
        ra_b = astropy.table.MaskedColumn.pformat(ra_a)
        ra_c = ra_b[2]
        ra_d = unicodedata.normalize('NFKD', ra_c).encode('ascii','ignore')
        ra_d_new = ra_d.replace(" ", ":")
        
        dec_a = result_table.columns[2]
        dec_b = astropy.table.MaskedColumn.pformat(dec_a)
        dec_c = dec_b[2]
        dec_d = unicodedata.normalize('NFKD', dec_c).encode('ascii','ignore')
        dec_d_new = dec_d.replace(" ", ":")
        
        f.write('%s,%s,%s\n' % (thisName, ra_d_new, dec_d_new))

    if result_table is None:
        print thisName, ' not found'

f.close()
