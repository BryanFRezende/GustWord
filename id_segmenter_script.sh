#!/bin/bash

j=100
k=200
l=500
m=1000
n=j+k+l+m

for ((i = 0; i < n; i++)); do
  read -r line
  if ((i >= 0)) && ((i < j))
  then  
    echo $line >> first_100_ids.csv
  elif ((i >= j)) && ((i < j+k))
  then
    echo $line >> second_200_ids.csv
  elif ((i >= j+k)) && ((i < j+k+l))
  then
    echo $line >> third_500_ids.csv
  elif ((i >= j+k+l))
  then
    echo $line >> fourth_1k_ids.csv
  fi
  done < City_IDs.csv

echo "Done."