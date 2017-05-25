#!/usr/bin/env python2.7

# This script converts reads in bed format to reads only containing an interval
# of one nucleotide encompassing the start site of the read. The output is also
# in bed format.
#
# Usage:
# read_cutter.py <input_reads.bed>

import sys
import io

# Checks to see if any files were supplied
if len(sys.argv) == 1:
    print("\nNo files supplied.\n\nUsage: read_cutter.py <reads.bed>\n")

input_reads = io.open(sys.argv[1], "rU")
output_reads = io.open("read_cutter_output.bed", "wb")

for line in input_reads:
    linestripped = line.strip()
    line_list = linestripped.split("\t")
    chromosome = line_list[0]
    strand = line_list[5]
    read_start = line_list[1]
    read_end = line_list[2]
    read_name = line_list[3]
    score = line_list[4]
    if strand == "+":
        new_read_start = read_start
        new_read_end = int(read_start) + 1
        output_reads.write(str(chromosome) + "\t" +
                           str(new_read_start) + "\t" + 
                           str(new_read_end) + "\t" +
                           str(read_name) + "\t" +
                           str(score)  + "\t" + 
                           str(strand) + "\n")
    if strand == "-":
        new_read_start = int(read_end) - 1
        new_read_end = read_end
        output_reads.write(str(chromosome) + "\t" +
                           str(new_read_start) + "\t" + 
                           str(new_read_end) + "\t" +
                           str(read_name) + "\t" +
                           str(score)  + "\t" + 
                           str(strand) + "\n")
input_reads.close()
output_reads.close()
