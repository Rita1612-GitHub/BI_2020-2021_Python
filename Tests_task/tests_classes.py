import unittest

from dna_rna_class import *


class TestDna(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestDna, cls).setUpClass()
        cls.cls = Dna
        cls.sequence = 'ATGGCCATTGTAATGGGCc'
        cls.another_sequence = 'GTGGCCATTGTAATGGGGG'

    def test_successful_init(self):
        instance = self.cls(self.sequence)
        self.assertEqual(instance._data, self.sequence)

    def test_failed_init(self):
        with self.assertRaises(TypeError):
            self.cls(1234)

    def test_str(self):
        instance = self.cls(self.sequence)
        self.assertEqual(str(instance), self.sequence)

    def test_hash(self):
        instance1 = self.cls(self.sequence)
        instance2 = self.cls(self.another_sequence)
        _set = {instance1, instance2}
        self.assertIn(instance1, _set)
        self.assertIn(instance2, _set)

    def test_equal(self):
        instance1 = self.cls(self.sequence)
        instance2 = self.cls(self.sequence)
        self.assertEqual(instance1, instance2)
        instance3 = self.cls(self.another_sequence)
        self.assertNotEqual(instance1, instance3)

    def test_len(self):
        instance = self.cls(self.sequence)
        self.assertEqual(len(instance), len(self.sequence))

    def test_iter(self):
        instance = self.cls(self.sequence)
        self.assertEqual([el for el in instance], list(self.sequence))

    def test_gc_content(self):
        instance = self.cls(self.sequence)
        self.assertAlmostEqual(instance.gc_content(), 52.63157894736842)

    def test_reverse_complement(self):
        instance = self.cls(self.sequence)
        self.assertEqual(instance.reverse_complement(), 'gGCCCATTACAATGGCCAT')

    def test_transcribe(self):
        instance = self.cls(self.sequence)
        result = instance.transcribe()
        self.assertIsInstance(result, Rna)
        self.assertEqual(str(result), 'AUGGCCAUUGUAAUGGGCc')


class TestRna(TestDna):
    @classmethod
    def setUpClass(cls):
        super(TestDna, cls).setUpClass()
        cls.cls = Rna
        cls.sequence = 'AUGGCCAUUGUAAUGGGCc'
        cls.another_sequence = 'GGGGCCAUUGUAAUGGGGG'

    def test_reverse_complement(self):
        instance = self.cls(self.sequence)
        self.assertEqual(instance.reverse_complement(), 'gGCCCUTTUCUUTGGCCUT')

    def test_transcribe(self):
        instance = self.cls(self.sequence)
        result = instance.transcribe()
        self.assertIsInstance(result, Dna)
        self.assertEqual(str(result), 'ATGGCCATTGTAATGGGCc')


if __name__ == '__main__':
    unittest.main()
