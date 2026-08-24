#!/bin/bash
ls /nonexistent_folder /tmp > out.txt 2> err.txt
ls /nonexistent_folder /tmp > all.txt 2>&1
