#C:\Users\kaiba\OneDrive\Asztali gép\learning-python\new.py

import pandas as pd

def main():
    filename = "Hungary-streets.xls"

    pd.read_excel(filename, index_col= 0)


if __name__ == "__main__":
    main()