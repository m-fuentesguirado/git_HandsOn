
### Cleaned-up Code Example:

```bash
#!/bin/bash

# Check if the sequence and motif are provided
if [[ -n $1 && -n $2 ]]; then
  seq=$1
  motif=$(echo $2 | tr a-z A-Z)  # Convert motif to uppercase for case-insensitive search

  echo -en "Motif search enabled: looking for motif '$motif' in sequence '$seq'..."

  # Search for motif in sequence
  if [[ $seq =~ $motif ]]; then
    echo "Motif '$motif' found in the sequence!"
  else
    echo "MOTIF NOT FOUND IN SEQUENCE"
  fi
else
  echo "No sequence or motif provided"
fi

echo "Search complete"

