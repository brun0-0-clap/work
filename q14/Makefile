.PHONY: all clean

all: report.txt

stats.txt: data.csv stats.py
	python3 stats.py

report.txt: stats.txt build_report.py report.md
	python3 build_report.py

clean:
	rm -f stats.txt report.txt
