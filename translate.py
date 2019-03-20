#! /usr/bin/env python3

import sys

def pop_next_codon(sequence):

    codon = sequence[0:3]
    remaining_seq = sequence[3:]
    return codon, remaining_seq

def translate_sequence(rna_sequence, genetic_code):
    """Translates a sequence of RNA into a sequence of amino acids.

    Translates `rna_sequence` into string of amino acids, according to the
    `genetic_code` given as a dict. Translation begins at the first position of
    the `rna_sequence` and continues until the first stop codon is encountered
    or the end of `rna_sequence` is reached.

    If `rna_sequence` is less than 3 bases long, or starts with a stop codon,
    an empty string is returned.
    """

#    if len(rna_sequence) < 3:
#        return ''
#    else:
#        sequence=rna_sequence.upper()
#        while len(sequence) >= 3:
#            codon = sequence[0:3]
#            sequence = sequence[3:]
#            if genetic_code[codon] =='*':
#                return ''
#            else:
#                return ''

    rna_sequence = rna_sequence.upper()
    amino_acid_list = []
    while True:
        if len(rna_sequence) < 3:
            break
        codon, remaining_seq = pop_next_codon(rna_sequence)
        rna_sequence = remaining_seq
        aa = genetic_code[codon]
        if aa == "*":
            break
        amino_acid_list.append(aa)
    return "".join(amino_acid_list)

def get_all_translations(rna_sequence, genetic_code):
    """Get a list of all amino acid sequences encoded by an RNA sequence.

    All three reading frames of `rna_sequence` are scanned from 'left' to
    'right', and the generation of a sequence of amino acids is started
    whenever the start codon 'AUG' is found. The `rna_sequence` is assumed to
    be in the correct orientation (i.e., no reverse and/or complement of the
    sequence is explored).

    The function returns a list of all possible amino acid sequences that
    are encoded by `rna_sequence`.

    If no amino acids can be translated from `rna_sequence`, an empty list is
    returned.
    """
    rna_sequence = rna_sequence.upper()
    number_of_bases = len(rna_sequence)
    last_codon_index = number_of_bases - 3
    if last_codon_index < 0:
        return[]
    amino_acid_seq_list = []
    for base_index in range(last_codon_index + 1):
        codon = rna_sequence[base_index: base_index + 3]
        if codon == "AUG":
            aa_seq = translate_sequence(
                rna_sequence = rna_sequence[base_index],
                genetic_code = genetic_code)
            if aa_seq:
                amino_acid_seq_list.append(aa_seq)
    return amino_acid_seq_list

def get_reverse(sequence):
    """Reverse orientation of `sequence`.

    Returns a string with `sequence` in the reverse order.

    If `sequence` is empty, an empty string is returned.
    """

#    sequence = rna_sequence.upper()
#    reverse_seq = sequence[::-1]
#    if len(sequence) == 0:
#        return ""
#    else:
#        return reverse_seq

# below is version Jamie wrote in class on Mar 6
#    sequence = sequence.upper()
#    rev_seq = ""
#    for c in sequence:
#        rev_seq = c + rev_seq
#    return rev_seq

    seq_list = list(sequence.upper())
    seq_list.reverse()
    rev_seq = "".join(seq_list)
    return rev_seq

def get_complement(sequence):
    """Get the complement of `sequence`.

    Returns a string with the complementary sequence of `sequence`.

    If `sequence` is empty, an empty string is returned.
    """

#    sequence = sequence.upper()
#    complement = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
#    return '' .join([complement[base] for base in sequence])

# below is version Jamie wrote in class on Mar 6

#    sequence = sequence.upper()
#    comp_bases = {
#        'A': 'U',
#        'U': 'A',
#        'G': 'C',
#        'C': 'G',
#        }
#    comp_seq = ""
#    for c in sequence:
#        comp_seq += comp_bases[c]
#    return comp_seq

    rna_complement = {
        'A': 'U',
        'C': 'G',
        'G': 'C',
        'U': 'A',
        }
    complementary_seq_list = []
    for character in sequence:
        complementary_seq_list.append(rna_complement[character.upper()])
    complementary_seq = "".join(complementary_seq_list)
    return complementary_seq

def reverse_and_complement(sequence):
    """Get the reversed and complemented form of `sequence`.

    Returns a string that is the reversed and complemented sequence
    of `sequence`.

    If `sequence` is empty, an empty string is returned.
    """
    # just runs through get_complement() and get_reverse()

#    complement=get_complement(sequence)
#    reverse_complement=get_reverse(complement)
#    return reverse_complement

#    return get_reverse(get_complement(sequence))
    
    reverse_seq = get_reverse(sequence)
    reverse_complement_seq = get_complement(reverse_seq)
    return reverse_complement_seq

def get_longest_peptide(rna_sequence, genetic_code):
    """Get the longest peptide encoded by an RNA sequence.

    Explore six reading frames of `rna_sequence` (three reading frames of the
    current orientation, and the reversed and complemented form) and return (as
    a string) the longest sequence of amino acids that it encodes, according to
    the `genetic_code`.

    If no amino acids can be translated from `rna_sequence` nor its reverse and
    complement, an empty list is returned.
    """
    peptides = get_all_translations(rna_sequence = rna_sequence, genetic_code = genetic_code)
    rev_comp_seq = reverse_and_complement(rna_sequence)
    rev_comp_peptides = get_all_translations(rna_sequence = rev_comp_seq, genetic_code = genetic_code)
    peptides += rev_comp_peptides
    if not peptides:
        return ""
    if len(peptides) < 2:
        return peptides[0]
    most_number_of_bases = -1
    longest_peptide_index = -1
    for peptide_index, aa_seq in enumerate(peptides):
        if len(aa_seq) > most_number_of_bases:
            longest_peptide_index = peptide_index
            most_number_of_bases = len(aa_seq)
    return peptides[longest_peptide_index]


if __name__ == '__main__':
    genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
    rna_seq = ("AUG"
            "UAC"
            "UGG"
            "CAC"
            "GCU"
            "ACU"
            "GCU"
            "CCA"
            "UAU"
            "ACU"
            "CAC"
            "CAG"
            "AAU"
            "AUC"
            "AGU"
            "ACA"
            "GCG")
    longest_peptide = get_longest_peptide(rna_sequence = rna_seq,
            genetic_code = genetic_code)
    assert isinstance(longest_peptide, str), "Oops: the longest peptide is {0}, not a string".format(longest_peptide)
    message = "The longest peptide encoded by\n\t'{0}'\nis\n\t'{1}'\n".format(
            rna_seq,
            longest_peptide)
    sys.stdout.write(message)
    if longest_peptide == "MYWHATAPYTHQNISTA":
        sys.stdout.write("Indeed.\n")
