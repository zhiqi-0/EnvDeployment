#!/bin/bash
for f in *.tar
do 
  d=`basename $f .tar`
  mkdir ../$d
  tar -xf $f -C ../$d
  rm $f
done
cd .. && rm -rf folder