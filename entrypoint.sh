#!/bin/sh

if [ -z "$1" ]
then
      echo "please enter MAC address as parameter"
else
    python get_company_name.py "$1"
fi
