def dna_to_rna(base):
    base = base.upper()
    new_base = ""
    for i in base:
        if i == "T":
            new_base += "U"
        else:
            new_base += i
    return new_base