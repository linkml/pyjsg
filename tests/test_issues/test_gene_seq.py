from pyjsg.validate_json import JSGPython


def test_gene_seq_test_1():
        x = JSGPython('''
doc {
    sequences: [(RNASEQ|DNASEQ)]
}

@terminals
RNASEQ: [ACGU]+ ;
DNASEQ: [ACGT]+ ;
''')

        rslt = x.conforms('''
{ "sequences": [
    "GCUACGGAGCUUGGAGCUAG",
    "ATTTTGCGAGGTCCC"
   ]
}''')
        assert rslt.success
