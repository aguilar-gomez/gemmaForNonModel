#!/usr/bin/env python
# Author : Diana Aguilar
'''script to modify association with gemma results, for assemblies with too many scaffolds for plink
Convert scaffolds to a single giant chromosome, re map to original names

Use re_map_names.py result_association easy_remapfile result_asso_original_chr
'''
import sys
import pandas as pd

filename=sys.argv[1]
easy_remap=sys.argv[2]
outfilename=sys.argv[3]

chrs=pd.read_csv(easy_remap,header=None,sep="\t")
#Dictionary with map positions ["giant_chr_rs"]="original_rs"
easy_remap_dic=chrs[[0,1]].set_index([1]).to_dict()

outfile= open(outfilename,"w+")
infile = open(filename, "r")

for line in infile:
	rs=line.split("\n")[0]
	merged_rs=easy_remap_dic[0][rs]
        outfile.write(merged_rs+"\n")

infile.close()
outfile.close()
