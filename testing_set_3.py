import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb3.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)


    def test1(self):
        ask1 = read.parse_input("fact: (different Nosliw Uzna)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])

    def test2(self):
        ask1 = read.parse_input("fact: (friendly Nosliw)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (friendly ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Uzna")
        self.assertEqual(str(answer[1]), "?X : Hershey")
        self.assertEqual(str(answer[2]), "?X : Ai")

    def test4(self):
        ask1 = read.parse_input("fact: (isa ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : dragon, ?Y : monster")
        self.assertEqual(str(answer[1]), "?X : giant, ?Y : monster")
        self.assertEqual(str(answer[2]), "?X : dog, ?Y : animal")

if __name__ == '__main__':
    unittest.main()
