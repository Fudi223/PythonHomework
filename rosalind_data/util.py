# a library of utility functions for Rosalind exercises

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped


def RNA_Rev(DNA):
    DNA = DNA.replace("T", "U")
print(RNA_Rev)