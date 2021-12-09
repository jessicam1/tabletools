import sys
import argparse

def get_input_file_object(filename):
    if filename == "-":
        return sys.stdin
    return open(filename, "r")

def parse_args(args):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--table", default='-', help="input csv file; STDIN if - (default: %(default)s)")
    parser.add_argument("-c", "--col-name", required=True, help="name for new column")
    parser.add_argument("-v", "--col-value", required=True, help="constant value for new column")
    parser.add_argument("-s", "--separator", default='\t', help="column separator character, default: <TAB>")
    parser.add_argument("--at-end", action="store_true", help="inserts new column as the right most one.")
    return parser.parse_args(args)

def add_col(table, sep, colname, colvalue, at_end):
    i = 0
    for line in table:
        line = line.rstrip('\n')
        if i==0:
            if at_end:
                print(line + sep + colname)
            else:
                print(colname + sep + line)
        else:
            if at_end:
                print(line + sep + colvalue)
            else:
                print(colvalue + sep + line)
        i += 1
    return 

def main():
    """
    Add a column containing a constant value to a table. Header assumed.
    """
    args = parse_args(sys.argv[1:])
    # print(sys.argv[1:])
    # print(args)
    table = get_input_file_object(args.table)
    add_col(table, args.separator, args.col_name, args.col_value, args.at_end)
    return

