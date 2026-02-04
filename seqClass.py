#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
#This code parse CLI arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
#This parts  converts input into uppercase
args.seq = args.seq.upper()                 

#This functions helps to  filter the characters that are allowed and classify DNA/RNA


if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and re.search ('U', args.seq):
        print ('The sequence is neither DNA nor RNA')
    elif re.search ('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence can be anything')
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("MOTIF FOUND, KEEP WORKING")
    else:
        print("MOTIF NOT FOUND")

