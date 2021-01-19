#!/usr/bin/env python
# Author : Diana Aguilar
'''script to modify map file, for assemblies with too many scaffolds for plink
Convert scaffolds to a single giant chromosome
Example:
chr1 1-10
chr2 1-9
chr3 1-8
To:
chr1-10
chr1 11-19
chr1 20-27

Use merge_chr_map.py mapfile reference.fasta.fai merged.mapfile easy_remapfile
'''
import sys
import pandas as pd

filename=sys.argv[1]
fasta_fai=sys.argv[2]
outfilename=sys.argv[3]
easy_remap=sys.argv[4]

chrs=pd.read_csv(fasta_fai,header=None,sep="\t")
chrs["start_pos"]=chrs[1].cumsum()-chrs[1]
#Dictionary with cumpos to access cum pos easy_access_cum["start_pos"]["chr#"]
easy_access_cum=chrs[[0,"start_pos"]].set_index([0]).to_dict()

#Open files
outfile= open(outfilename,"w+")
remapfile= open(easy_remap,"w+")
infile = open(filename, "r")

for line in infile:
	column=line.split("\t")
	chr_and_pos=column[1].split(":")
	chrom=chr_and_pos[0]
	newposition=int(chr_and_pos[1])+easy_access_cum["start_pos"][chrom]
	outfile.write('\t'.join(["1","chr1:"+str(newposition),"0",str(newposition)])+"\n")
	remapfile.write('\t'.join(["chr1:"+str(newposition),chrom+":"+chr_and_pos[1]])+"\n")

infile.close()
outfile.close()
remapfile.close()
