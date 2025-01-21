import argparse

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description='Example script demonstrating common argparse features',
        epilog='Thanks for using this script!'
    )

    # Required positional argument
    parser.add_argument('filename', help='Input file to process')

    # Optional argument with a default value
    parser.add_argument('-n', '--number', type=int, default=10,
                        help='Number of lines to process (default: 10)')

    # Flag argument (True/False)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Increase output verbosity')

    # Choice from a list of options
    parser.add_argument('--mode', choices=['read', 'write', 'append'],
                        default='read', help='File operation mode')

    # Multiple values
    parser.add_argument('--files', nargs='+',
                        help='Multiple files to process')

    # Optional argument with specific type
    parser.add_argument('--threshold', type=float, default=0.5,
                        help='Threshold value (float between 0 and 1)')

    # Parse the arguments
    args = parser.parse_args()

    # Example usage of parsed arguments
    if args.verbose:
        print(f"Processing {args.filename}")
        print(f"Mode: {args.mode}")
        print(f"Number of lines: {args.number}")
        print(f"Threshold: {args.threshold}")
        if args.files:
            print(f"Additional files: {args.files}")

if __name__ == '__main__':
    main()

# Example command line usage:
# python script.py input.txt -n 20 --verbose --mode write --files file1.txt file2.txt --threshold 0.75