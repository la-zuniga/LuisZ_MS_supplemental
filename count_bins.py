# script to make a table of MAG taxonomy and bin counts in each sample


import os
import glob
import re
import argparse
import pandas as pd


# making a function to readlines in bin summaries
def read_bin_summary(bin_summary):
    with open(bin_summary, 'r') as f:
        bin_summary_lines = f.readlines()
    return bin_summary_lines

# reading in the 12 bin summaries
Acau1 = read_bin_summary('Acau1_summary.txt')
Acau2 = read_bin_summary('Acau2_summary.txt')
Acon1 = read_bin_summary('Acon1_summary.txt')
Acon2 = read_bin_summary('Acon2_summary.txt')
Acon3 = read_bin_summary('Acon3_summary.txt')
Acra1 = read_bin_summary('Acra1_summary.txt')
Aful2 = read_bin_summary('Aful2_summary.txt')
Xmut1 = read_bin_summary('Xmut1_summary.txt')
Xmut2 = read_bin_summary('Xmut2_summary.txt')
Wfilter1 = read_bin_summary('Wfilter1_summary.txt')
Wfilter2 = read_bin_summary('Wfilter2_summary.txt')
Wfilter3 = read_bin_summary('Wfilter3_summary.txt')

# making a function to remove ;s and the rest of the line after the ;c
# and remove ;p__ and everything before it
# this leaves each line with sp_binname and taxonomy up to genus

def remove_semicolon(bin_summary_lines):
      bin_summary_lines = [re.sub(r';o.*', '', line) for line in bin_summary_lines]
      return bin_summary_lines


# updated bin summaries
Acau1 = remove_semicolon(Acau1)
Acau2 = remove_semicolon(Acau2)
Acon1 = remove_semicolon(Acon1)
Acon2 = remove_semicolon(Acon2)
Acon3 = remove_semicolon(Acon3)
Acra1 = remove_semicolon(Acra1)
Aful2 = remove_semicolon(Aful2)
Xmut1 = remove_semicolon(Xmut1)
Xmut2 = remove_semicolon(Xmut2)
Wfilter1 = remove_semicolon(Wfilter1)
Wfilter2 = remove_semicolon(Wfilter2)
Wfilter3 = remove_semicolon(Wfilter3)

# make dictionaries of bin names and taxonomy
def make_dict(bin_summary_lines):
    bin_summary_dict = {}
    for line in bin_summary_lines:
        bin_summary_dict[line.split()[0]] = line.split()[1]
    return bin_summary_dict

# updated bin summaries
Acau1_dict = make_dict(Acau1)
Acau2_dict = make_dict(Acau2)
Acon1_dict = make_dict(Acon1)
Acon2_dict = make_dict(Acon2)
Acon3_dict = make_dict(Acon3)
Acra1_dict = make_dict(Acra1)
Aful2_dict = make_dict(Aful2)
Xmut1_dict = make_dict(Xmut1)
Xmut2_dict = make_dict(Xmut2)
Wfilter1_dict = make_dict(Wfilter1)
Wfilter2_dict = make_dict(Wfilter2)
Wfilter3_dict = make_dict(Wfilter3)


# a function to get the taxonomies from the dictionaries

def get_tax_names(bin_summary_dict):
    tax_names = []
    for key in bin_summary_dict:
        tax_names.append(bin_summary_dict[key])
    return tax_names

# getting the taxonomies from the dictionaries

Acau1_tax_names = get_tax_names(Acau1_dict)
Acau2_tax_names = get_tax_names(Acau2_dict)
Acon1_tax_names = get_tax_names(Acon1_dict)
Acon2_tax_names = get_tax_names(Acon2_dict)
Acon3_tax_names = get_tax_names(Acon3_dict)
Acra1_tax_names = get_tax_names(Acra1_dict)
Aful2_tax_names = get_tax_names(Aful2_dict)
Xmut1_tax_names = get_tax_names(Xmut1_dict)
Xmut2_tax_names = get_tax_names(Xmut2_dict)
Wfilter1_tax_names = get_tax_names(Wfilter1_dict)
Wfilter2_tax_names = get_tax_names(Wfilter2_dict)
Wfilter3_tax_names = get_tax_names(Wfilter3_dict)

# make a list of all the taxonomies
all_tax = Acau1_tax_names + Acau2_tax_names + Acon1_tax_names + Acon2_tax_names + Acon3_tax_names + Acra1_tax_names + Aful2_tax_names + Xmut1_tax_names + Xmut2_tax_names + Wfilter1_tax_names + Wfilter2_tax_names + Wfilter3_tax_names
# remove duplicates
all_tax = list(set(all_tax))

# make a list of sample names
sample_names = ['Acau1', 'Acau2', 'Acon1', 'Acon2', 'Acon3', 'Acra1', 'Aful2', 'Xmut1', 'Xmut2', 'Wfilter1', 'Wfilter2', 'Wfilter3']

# count how many times each taxonomy appears in each sample 
def count_tax(bin_summary_dict, all_tax):
    tax_count = []
    for tax in all_tax:
        count = 0
        for key in bin_summary_dict:
            if bin_summary_dict[key] == tax:
                count += 1
        tax_count.append(count)
    return tax_count

# getting the counts for each sample
Acau1_tax_count = count_tax(Acau1_dict, all_tax)
Acau2_tax_count = count_tax(Acau2_dict, all_tax)
Acon1_tax_count = count_tax(Acon1_dict, all_tax)
Acon2_tax_count = count_tax(Acon2_dict, all_tax)
Acon3_tax_count = count_tax(Acon3_dict, all_tax)
Acra1_tax_count = count_tax(Acra1_dict, all_tax)
Aful2_tax_count = count_tax(Aful2_dict, all_tax)
Xmut1_tax_count = count_tax(Xmut1_dict, all_tax)
Xmut2_tax_count = count_tax(Xmut2_dict, all_tax)
Wfilter1_tax_count = count_tax(Wfilter1_dict, all_tax)
Wfilter2_tax_count = count_tax(Wfilter2_dict, all_tax)
Wfilter3_tax_count = count_tax(Wfilter3_dict, all_tax)

# make a dataframe of the counts for where samples are rows and taxonomies are columns
df = pd.DataFrame([Acau1_tax_count, Acau2_tax_count, Acon1_tax_count, Acon2_tax_count, Acon3_tax_count, Acra1_tax_count, Aful2_tax_count, Xmut1_tax_count, Xmut2_tax_count, Wfilter1_tax_count, Wfilter2_tax_count, Wfilter3_tax_count], columns = all_tax, index = sample_names)
# write the dataframe to a csv
df.to_csv('bin_counts_phylum.csv')

