#! /usr/bin/env python3

import unittest

import translate

class TestTranslateBaseClass(unittest.TestCase):
    def setUp(self):
        self.genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}

    def run_translate_sequence(self, rna_seq,
            expected_amino_acid_seq,
            gen_code = None):
        if gen_code is None:
            gen_code = self.genetic_code
        amino_acid_seq = translate.translate_sequence(
                rna_sequence = rna_seq,
                genetic_code = gen_code)
        message = (
                "\n\n"
                "Calling `translate_sequence` with `rna_sequence`:\n"
                "\t{0!r}\n"
                "Expecting {1!r}, but {2!r} was returned".format(
                        rna_seq,
                        expected_amino_acid_seq,
                        amino_acid_seq))
        self.assertEqual(amino_acid_seq, expected_amino_acid_seq, message)

    def run_get_all_translations(self, rna_seq,
            expected_results,
            gen_code = None):
        if gen_code is None:
            gen_code = self.genetic_code
        amino_acid_seqs = translate.get_all_translations(
                rna_sequence = rna_seq,
                genetic_code = gen_code)
        message = (
                "\n\n"
                "Calling `get_all_translations` with `rna_sequence`:\n"
                "\t{0!r}\n"
                "Expecting {1!r}, but {2!r} was returned".format(
                        rna_seq,
                        expected_results,
                        amino_acid_seqs))
        if amino_acid_seqs:
            amino_acid_seqs = sorted(amino_acid_seqs)
        if expected_results:
            expected_results = sorted(expected_results)
        self.assertEqual(amino_acid_seqs, expected_results, message)

    def run_get_reverse(self, seq, expected_result):
        rev_seq = translate.get_reverse(seq)
        message = (
                "\n\n"
                "Calling `get_reverse` with argument:\n"
                "\t{0!r}\n"
                "Expecting\n"
                "\t{1!r}\n"
                "to be returned, but got\n"
                "\t{2!r}\n".format(
                        seq,
                        expected_result,
                        rev_seq))
        self.assertEqual(rev_seq, expected_result, message)

    def run_get_complement(self, seq, expected_result):
        comp_seq = translate.get_complement(seq)
        message = (
                "\n\n"
                "Calling `get_complement` with argument:\n"
                "\t{0!r}\n"
                "Expecting\n"
                "\t{1!r}\n"
                "to be returned, but got\n"
                "\t{2!r}\n".format(
                        seq,
                        expected_result,
                        comp_seq))
        self.assertEqual(comp_seq, expected_result, message)

    def run_reverse_and_complement(self, seq, expected_result):
        rc_seq = translate.reverse_and_complement(seq)
        message = (
                "\n\n"
                "Calling `reverse_and_complement` with argument:\n"
                "\t{0!r}\n"
                "Expecting\n"
                "\t{1!r}\n"
                "to be returned, but got\n"
                "\t{2!r}\n".format(
                        seq,
                        expected_result,
                        rc_seq))
        self.assertEqual(rc_seq, expected_result, message)

    def run_get_longest_peptide(self, rna_seq,
            expected_result,
            gen_code = None):
        if gen_code is None:
            gen_code = self.genetic_code
        amino_acid_seq = translate.get_longest_peptide(
                rna_sequence = rna_seq,
                genetic_code = gen_code)
        message = (
                "\n\n"
                "Calling `get_longest_peptide` with `rna_sequence`:\n"
                "\t{0!r}\n"
                "Expecting {1!r}, but {2!r} was returned".format(
                        rna_seq,
                        expected_result,
                        amino_acid_seq))
        self.assertEqual(amino_acid_seq, expected_result, message)


class TestTranslateSequence(TestTranslateBaseClass):

    def test_empty_rna_sequence(self):
        rna_seq = ""
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_rna_sequence_with_one_base(self):
        rna_seq = "A"
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_rna_sequence_with_two_bases(self):
        rna_seq = "AG"
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_only_stop_codon(self):
        rna_seq = "UGA"
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_one_codon(self):
        rna_seq = "GUC"
        expected_amino_acid_seq = "V"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

        rna_seq = "GAA"
        expected_amino_acid_seq = "E"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_one_codon_lower_case(self):
        rna_seq = "guc"
        expected_amino_acid_seq = "V"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

        rna_seq = "gaa"
        expected_amino_acid_seq = "E"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_no_stop_to_end(self):
        rna_seq = "GUCGAACGA"
        expected_amino_acid_seq = "VER"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_no_stop_with_extra_base(self):
        rna_seq = "GUCGAACGAA"
        expected_amino_acid_seq = "VER"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_stop_codon_at_end(self):
        rna_seq = "GUCGAACGAUAA"
        expected_amino_acid_seq = "VER"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_stop_codon_within(self):
        rna_seq = "GUCGAAUAACGA"
        expected_amino_acid_seq = "VE"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)


class TestGetAllTranslations(TestTranslateBaseClass):

    def test_no_translations(self):
        rna_seq = "GUCGAAUAACGA"
        expected_amino_acid_seqs = []
        self.run_get_all_translations(
                rna_seq = rna_seq,
                expected_results = expected_amino_acid_seqs)

    def test_one_start_at_end(self):
        rna_seq = "GUCGAAUAACGAAUG"
        expected_amino_acid_seqs = ["M"]
        self.run_get_all_translations(
                rna_seq = rna_seq,
                expected_results = expected_amino_acid_seqs)

    def test_two_short_peptides(self):
        rna_seq = "CCUGAAUGACGUACGUAUGACUGCAGUACGUUACGUACG"
        expected_amino_acid_seqs = [
                "MTYV",
                "MTAVRYV",
                ]
        self.run_get_all_translations(
                rna_seq = rna_seq,
                expected_results = expected_amino_acid_seqs)

    def test_two_short_peptides_lower_case(self):
        rna_seq = "ccugaaugacguacguaugacugcaguacguuacguacg"
        expected_amino_acid_seqs = [
                "MTYV",
                "MTAVRYV",
                ]
        self.run_get_all_translations(
                rna_seq = rna_seq,
                expected_results = expected_amino_acid_seqs)

    def test_two_short_peptides_at_beginning(self):
        rna_seq = "AUGACGUACGUAUGACUGCAGUACGUUACGUACG"
        expected_amino_acid_seqs = [
                "MTYV",
                "MTAVRYV",
                ]
        self.run_get_all_translations(
                rna_seq = rna_seq,
                expected_results = expected_amino_acid_seqs)


class TestGetReverse(TestTranslateBaseClass):
    def test_empty_string(self):
        seq = ""
        expected_result = ""
        self.run_get_reverse(seq, expected_result)

    def test_one_base(self):
        seq = "A"
        expected_result = "A"
        self.run_get_reverse(seq, expected_result)

    def test_simple(self):
        seq = "AUGC"
        expected_result = "CGUA"
        self.run_get_reverse(seq, expected_result)

    def test_simple_lower_case(self):
        seq = "augc"
        expected_result = "CGUA"
        self.run_get_reverse(seq, expected_result)


class TestGetComplement(TestTranslateBaseClass):
    def test_empty_string(self):
        seq = ""
        expected_result = ""
        self.run_get_complement(seq, expected_result)

    def test_one_base(self):
        seq = "G"
        expected_result = "C"
        self.run_get_complement(seq, expected_result)

    def test_simple(self):
        seq = "AUGC"
        expected_result = "UACG"
        self.run_get_complement(seq, expected_result)

    def test_simple_lower_case(self):
        seq = "augc"
        expected_result = "UACG"
        self.run_get_complement(seq, expected_result)


class TestReverseAndComplement(TestTranslateBaseClass):
    def test_empty_string(self):
        seq = ""
        expected_result = ""
        self.run_reverse_and_complement(seq, expected_result)

    def test_one_base(self):
        seq = "A"
        expected_result = "U"
        self.run_reverse_and_complement(seq, expected_result)

    def test_simple(self):
        seq = "AUGC"
        expected_result = "GCAU"
        self.run_reverse_and_complement(seq, expected_result)

    def test_simple(self):
        seq = "augc"
        expected_result = "GCAU"
        self.run_reverse_and_complement(seq, expected_result)


class TestGetLongestPeptide(TestTranslateBaseClass):

    def test_no_translations(self):
        rna_seq = "GUCGAAUAACGA"
        # UCGUUAUUCGAC
        expected_amino_acid_seq = ""
        self.run_get_longest_peptide(
                rna_seq = rna_seq,
                expected_result = expected_amino_acid_seq)

    def test_one_start_at_end(self):
        rna_seq = "GUCGAAUAACGAAUG"
        # CAUUCGUUAUUCGAC
        expected_amino_acid_seq = "M"
        self.run_get_longest_peptide(
                rna_seq = rna_seq,
                expected_result = expected_amino_acid_seq)

    def test_two_short_peptides(self):
        rna_seq = "CCUGAAUGACGUACGUAUGACUGCAGUACGUUACGUACG"
        #          CGUACGUAACGUACUGCAGUCAUACGUACGUCAUUCAGG
        expected_amino_acid_seq = "MTAVRYV"
        self.run_get_longest_peptide(
                rna_seq = rna_seq,
                expected_result = expected_amino_acid_seq)

    def test_two_short_peptides_in_rev_comp(self):
        rna_seq = "CGUACGUAACGUACUGCAGUCAUACGUACGUCAUUCAGG"
        #         "CCUGAAUGACGUACGUAUGACUGCAGUACGUUACGUACG"
        expected_amino_acid_seq = "MTAVRYV"
        self.run_get_longest_peptide(
                rna_seq = rna_seq,
                expected_result = expected_amino_acid_seq)

    def test_two_short_peptides_lower_case(self):
        rna_seq = "ccugaaugacguacguaugacugcaguacguuacguacg"
        #          CGUACGUAACGUACUGCAGUCAUACGUACGUCAUUCAGG
        expected_amino_acid_seq = "MTAVRYV"
        self.run_get_longest_peptide(
                rna_seq = rna_seq,
                expected_result = expected_amino_acid_seq)


if __name__ == '__main__':
    unittest.main() 
