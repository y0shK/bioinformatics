# wrapped genome, skew diagrams, etc.

# find occurrences of each nucleotide given a wrapped genome
# given a wrapped genome, account for the fact that it is wrapped and the 'sliding window' across the genome is large

def symbol_in_wrapped_genome(genome, nucleotide_length, symbol):

    wrapped_genome = genome + genome[0:len(genome) // 2] # need integer division in case nucleotideCount is not even

    symbol_dict = {}
    symbol_count_local = 0

    for i in range(len(wrapped_genome)):
        sliding_window = wrapped_genome[i:i+nucleotide_length]

        if len(sliding_window) == 4:
            for char in sliding_window:
                if char == symbol:
                    symbol_count_local = symbol_count_local + 1

        symbol_dict[i] = symbol_count_local
        # re-assign 0 to symbol count because we only care about the symbol count for each k-length nucleotide

        symbol_count_local = 0

        # ensure that we only find keys (or instances of cytosine) for the length of the genome
        if len(symbol_dict.keys()) == len(genome):
            break

    print(symbol_dict)

symbol_in_wrapped_genome('AAAAGGGG', 4, 'A')
