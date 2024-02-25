#!/bin/bash

output=`find . -type f -size +10M -not -path "./.venv/*" -exec ls -lh {} \; | awk '{ print substr($0, index($0,$9)) " || Size : " $5 }'`

if [[ ${#output} > 0 ]]; then
  echo $output
  echo "ERROR: There are files over the allowed limit of 10Mb. Please reduce their size or "
  EXIT_STATUS=1
else
  EXIT_STATUS=0
fi

exit $EXIT_STATUS