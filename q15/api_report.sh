#!/bin/bash

curl -fsS http://127.0.0.1:8000/packages.json > raw.json

jq -r '
  [.[] | select(.status=="active" and .downloads >= 100)]
  | sort_by(-.downloads, .name)
  | ["name","version","downloads"],
    ["---","---","---"],
    (.[] | [.name,.version,.downloads])
    | @tsv
' raw.json | awk -F'\t' '{print "| "$1" | "$2" | "$3" |"}' > summary.md

sed -i '1i# Active Packages Summary' summary.md
