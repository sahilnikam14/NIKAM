#!/bin/bash

clear
echo "=============================="
echo "   NIKAM HACKER"
echo "=============================="

read -p "Enter common word (ex: india): " word
read -p "Enter year (ex: 2005): " year

output="big_wordlist.txt"

# sample name list (expandable)
names=(
rahul rohit amit sumit akash vijay ajay karan arjun
sachin virat dhoni suraj pratik nikhil tejas omkar
aniket swapnil sagar harsh deepak yash raj
)

echo "Generating big wordlist..."

> $output

for name in "${names[@]}"
do
  echo "$name" >> $output
  echo "$name$year" >> $output
  echo "$name@123" >> $output
  echo "$name$word" >> $output
  echo "$name$year$word" >> $output
  echo "$name123" >> $output
  echo "$name@2024" >> $output
done

echo "Wordlist saved in $output"
