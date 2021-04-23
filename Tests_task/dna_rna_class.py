
dna_complement = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A",
    "N": "N",
}

rna_complement = {
    "A": "U",
    "C": "G",
    "G": "C",
    "U": "A",
    "N": "N",
}


def _maketrans(complement_mapping):
    before = "".join(complement_mapping.keys())
    after = "".join(complement_mapping.values())
    before += before.lower()
    after += after.lower()
    return str.maketrans(before, after)


_dna_complement_table = _maketrans(dna_complement)
_rna_complement_table = _maketrans(rna_complement)


class Dna:
    def __init__(self, data: str):
        if not isinstance(data, str):
            raise TypeError('It is not string')
        self._data: str = data

    def __str__(self):
        return self._data

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, obj):
        return str(self) == str(obj)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        i = 0
        while i < len(self):
            yield self._data[i]
            i += 1

    def gc_content(self) -> float:
        gc = sum(self._data.count(base) for base in ("G", "C", "g", "c", "N"))
        length = len(self._data)
        return gc * 100.0 / length if length else 0.0

    def reverse_complement(self):
        return str(self).translate(_dna_complement_table)[::-1]

    def transcribe(self):
        return Rna(str(self).replace("T", "U").replace("t", "u"))


class Rna(Dna):
    def transcribe(self):
        return Dna(str(self).replace("U", "T").replace("u", "t"))


def main():
    coding_dna = Dna("ATGGCCATTGTAATGGGCc")
    coding_dna2 = Dna("ATGGCCATTGTAATGGGCA")
    print(coding_dna.gc_content())
    print(coding_dna.transcribe())
    print(coding_dna.reverse_complement())
    print(coding_dna == coding_dna2)
    for x in {coding_dna, coding_dna2}: #приведение к строке
        print(x)

    for b in coding_dna: #итератор
        print(b)


if __name__ == "__main__":
    main()
