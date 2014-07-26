#!/bin/bash

fibos=( 1 2 )
last=2
sum=2

while [[ $last -le 4000000 ]]
do
	last=$((${fibos[-1]}+${fibos[-2]}))
	fibos+=($last)
	if [[ $(($last % 2)) -eq 0 ]]; then
		sum=$(($sum+$last))
	fi
done

echo "sum=$sum"
