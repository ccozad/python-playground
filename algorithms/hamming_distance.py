# The hamming distance is a measure of how different
# two equal length strings are. Each difference adds
# to the distance. The hamming distance only looks at
# matching character positions and does not try to
# shift either input to judge insertions and deletions.
class HammingDistance:
    def calculate(self, string1, string2):
        if len(string1) == len(string2):
            differences = 0
            for n in range(len(string1)):
                if string1[n] != string2[n]:
                    differences += 1
            
            return differences
        else:
            raise ValueError('Input strings must be the same length')