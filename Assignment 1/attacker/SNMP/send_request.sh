#!/bin/bash
time=0.5

if [ ! "$@" = "" ]
then
	time=$@
fi

while true
do
	snmpwalk -v 2c -c public 172.17.0.2 
	sleep "$time"
done
