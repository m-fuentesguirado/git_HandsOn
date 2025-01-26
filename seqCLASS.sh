#!/bin/bash
seq=$1
seq=$(echo $seq | tr a-z A-Z)  # Note we just added this line
if [[ $seq =~ ^[ACGTU]+$ ]]; then
  if [[ $seq =~ T ]]; then
    echo "The sequence is DNA"
  elif [[ $seq =~ U ]]; then
    echo "The sequence is RNA"
  else
    echo "The sequence can be DNA or RNA"
  fi
else
  echo "The sequence is not DNA nor RNA"
fi
# Adding motif search functionality
motif=$2
if [[ -n $motif ]]; then
  if [[ $seq == *$motif* ]]; then
    echo "Motif '$motif' found in the sequence"
  else
    echo "Motif '$motif' not found in the sequence"
  fi
else
  echo "No motif provided to search for"
fi

motif=$(echo $2 | tr a-z A-Z)
if [[ -n $motif ]]; then
  echo -en "Motif search enabled: looking for motif '$motif' in sequence '$seq'... "
  if [[ $seq =~ $motif ]]; then
    echo "Motif is located in the sequence!"
  else
    echo "NOT FOUND"
  fi
fi
echo "FOUND"
