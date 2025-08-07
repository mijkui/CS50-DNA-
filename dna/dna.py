import csv
import sys


def main():

    # TODO: Check for command-line usage

    # 1. Check for correct usage
    # Let user for typing python dna.py databases/small.csv sequences/1.txt
    # Therefore, three command-line argument


    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Grad the two filenames
    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # TODO: Read database file into a variable

    # 2. Read database into memory
    with open (database_filename) as db_file: # Necessary to give the csv file a variable name
        # Use Python’s csv.DictReader to load all the rows into a list of dicts
        reader = csv.DictReader(db_file) # Take the first row of the list become the key

        # Extract str
        str_names = reader.fieldnames[1:] # skip name

        # Make another list that have the dictionary (reader) becomes the list
        people = list (reader)



    # TODO: Read DNA sequence file into a variable

    # 3. Load the entire DNA sequence into memory as a single string so you can analyze it

    # Open the DNA sequence file and assign a variable to it
    with open (sequence_filename)as seq_file:

        # .read() -> Reads the entire contents of the file as one big string
        # This reads the entire contents of the file as one big string.
        # From AGATAGATAGATAATGTATC to 'AGATAGATAGATAATGTATC'


        # .strip() -> Removes any leading or trailing whitespace
        dna_sequence = seq_file.read().strip()


    # TODO: Find longest match of each STR in DNA sequence

    # 4. Build a dict mapping sequence STR
    str_count = {}

    for subseq in str_names:
        str_count[subseq] = longest_match (dna_sequence, subseq)
    # Looping over the dna_sequence by the subseq (which is the name AGAT, AATG, TATC) and count each number
    # str_count[subseq] is the dictionary organized afterward

    # TODO: Check database for matching profiles

    # 5. Check if the dna_sequence is matched with the people
    for person in people:
        match = True
        for subseq in str_names:
            # database values are strings, so convert to int
            # Check the perosn by the matching of STR
            if int(person[subseq]) != str_count[subseq]:
                match = False
                break
        if match:
            print(person["name"])
            return
    print (" No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

if __name__ == "__main__":
    main()
