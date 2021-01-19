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
easy_remap_dic=chrs[[0,1]].set_index([0]).to_dict()

outfile= open(outfilename,"w+")
infile = open(filename, "r")
#first line header
next(infile)
outfile.write("\t".join(["chr","rs","ps","n_mis","n_obs","allele1","allele0","af","beta","se","p_wald","p_lrt","p_score","original_rs","original_chr","original_pos"])+"\n")

for line in infile:
	column=line.split("\t")
	rs_format=column[1]
	original_rs=easy_remap_dic[1][rs_format]
	chr_and_pos=original_rs.split(":")
        outfile.write('\t'.join(column[:-1]+[column[-1].rstrip(),original_rs,chr_and_pos[0],chr_and_pos[1]])+"\n")


infile.close()
outfile.close()
