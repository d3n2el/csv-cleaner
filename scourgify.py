import csv
import sys
import os
def main():
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)< 3:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.exists(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]} ")
    else:
        with open(f"{sys.argv[1]}") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)


main()
