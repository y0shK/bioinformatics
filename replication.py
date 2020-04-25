# this code's ideas come from the Coursera course Bioinformatics for Beginners by UCSD
# except for the first function pattern_count, all of this code is original

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

# function that takes any string to find a dictionary of frequencies of k-mer
def frequency_given_k(string, k):
    string_array_fn = []

    for a in range(len(string) + 1):
        new_substring = string[a:a+k]
        string_array_fn.append(new_substring)
        a = a-1  # decrement by 1 so that the last letter of each substring repeats; e.g. ATA -> ATC, not TCC

    dict = {}

    for b in range(len(string_array_fn)):
        #print(string_array_fn[b])
        if string_array_fn[b] not in dict.keys():  # if the checked 3-mer is not in the keys, i.e. original
            dict[string_array_fn[b]] = 1  # it has a frequency of 1; it is new
        elif string_array_fn[b] in dict.keys():  # if the checked 3-mer IS in the keys, i.e. it has been spotted before
            dict[string_array_fn[b]] = dict[string_array_fn[b]] + 1  # increment the frequency it already has, we have spotted another occurrence
    return dict

# function that finds the max frequency 
def find_max_frequency_of_words(dict_provided):
    max_freq = max(dict_provided.values())
    print(max_freq)

    # get dictionary key directly as a variable
    # https://stackoverflow.com/questions/3545331/how-can-i-get-dictionary-key-as-variable-directly-in-python-not-by-searching-fr
    frequent_text = []
    for key, value in dict_provided.items():
        if value == max_freq: # is the frequency of the current k-length string equal to the max frequency?
            frequent_text.append(key) # if yes, note the k-length string for which that is true
    print(frequent_text)

# print max frequencies of various k-length strings
# wrap the frequency_given_k function into max_frequency to use the dictionary from the first function
	# function composition is necessary to pass variables without class instantiation
find_max_frequency_of_words(frequency_given_k('CGATATATCCATAG', 3))
find_max_frequency_of_words(frequency_given_k('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))

# apply solutions to Frequent Words Problem - Text = oriC of cholerae and k = 10
frequent_words_problem_text = cholerae_str
frequent_words_problem_k = 10

find_max_frequency_of_words(frequency_given_k(frequent_words_problem_text, frequent_words_problem_k))
print('\n')

# reverse complement problem - find reverse complenet of DNA string
# given Pattern, return reverse complement of Pattern

def reverse_complement_pattern(dna_string):
    """
    Reverse complement strategy - take the string, reverse it, find the complement, return the complement

    reverse string - because original strand is read 5' to 3', so Python accounts for that by reversing the string
        how to reverse? use slice notation
        slice notation works with string[beginning:end:n], leaving beginning and end blank ensures first and last param
        -1 for n indicates that the whole string is included - last character first, ..., first character last
    https://stackoverflow.com/questions/931092/reverse-a-string-in-python

    find the complement - for every 'A' append 'T', etc.
        how to find the complement? use a dictionary.
        for key, value in character -> for every key == 'A', value == 'T', etc.
    https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters
    """
    print('DNA string given: ' + dna_string)

    # break the string into components of characters for the for loop
    # replace each nucleotide with its complement one by one
    dna_string_reversed = dna_string[::-1]
    dna_string_reversed_components = list(dna_string_reversed)

    new_dna_string_components = []
    dna_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    for char in dna_string_reversed_components:
        for key, value in dna_dict.items():
            if char == key: # find which index this specific character in the reversed string belongs to
                new_dna_string_components.append(value) # find the nucleotide for that specific index

    # rejoin the broken string, put together all the nucleotides
    dna_complement_string = ''.join(new_dna_string_components)
    print('Complement of DNA string given: ' + dna_complement_string + '\n')

reverse_complement_pattern('AGT')
reverse_complement_pattern('AAAACCCGGT')

# Pattern Matching Problem - given a pattern and genome, find all 'first indices' where pattern is
# find where pattern is a subset of genome using string[i:i+k] = pattern
# this if statement goes through all possible permutations; 1:4, 2:6, 3:7, etc.
def pattern_matching(pattern, genome):
    positions_matching = [] # append the first nucleotide where the pattern is found in the genome
    iteration_amount = len(pattern) # find the number of characters to move to after the first position match

    for i in range(len(genome)): # go through all characters in the genome
        if genome[i:i + iteration_amount] == pattern: # does the pattern match this specific slice of the genome?
            positions_matching.append(i) # if yes, record this
    return positions_matching

print(pattern_matching('ATAT', 'GATATATGCATATACTT'))
print(pattern_matching('CTTGATCAT', 'CTTGATCATCTTGATCATCTTGATCAT'))
