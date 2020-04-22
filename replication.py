# code inspired by Bioinformatics for Beginners on Coursera
# with my own twists and original ideas thrown in

# find length of ori in Vibrio cholerae ori

cholerae_str = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
print(len(cholerae_str))

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1): # range wants the index after the index where iteration stops, add 1
        if text[i:i+len(pattern)] == pattern: # range from start to stop == pattern
            # ensures that index starts at the same index it stopped at, no skips
            count = count + 1 # frequency increases by 1
    return count

print(pattern_count(cholerae_str, "TGATCA"))

string_array = [] # empty array of strings to hold all the k-mers

for i in range(len(cholerae_str)+1):
    new_substring = cholerae_str[i:i+3] # can change index amount for k-mer
    string_array.append(new_substring)
    i = i-1 # decrement by 1 so that the last letter of each substring repeats; e.g. ATA -> ATC, not TCC

print(string_array)

freq = {} # empty dictionary for each set of k-mers

for i in range(len(string_array)):
    print(string_array[i])
    if string_array[i] not in freq.keys(): # if the checked 3-mer is not in the keys, i.e. original
        freq[string_array[i]] = 1 # it has a frequency of 1; it is new
    elif string_array[i] in freq.keys(): # if the checked 3-mer IS in the keys, i.e. it has been spotted before
        freq[string_array[i]] = freq[string_array[i]]+1 # increment the frequency it already has, we have spotted another occurrence

print(freq)
