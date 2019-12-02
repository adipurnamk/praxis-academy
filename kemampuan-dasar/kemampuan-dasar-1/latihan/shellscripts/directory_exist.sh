#!/bin/bash
echo "Enter diectory name"
read ndir
if [ -d "$ndir" ]
then
echo "Directory exist"
else
mkdir $ndir
echo "Directory created"
fi
