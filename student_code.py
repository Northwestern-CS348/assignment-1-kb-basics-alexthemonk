import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if not isinstance(fact, Fact):
            print("Assertion Failed: input not a Fact")
        elif fact in self.facts:
            print("Assertion Failed: input fact already exist")
        else:
            print("Asserting {!r}".format(fact))
            self.facts.append(fact)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        if isinstance(fact, Fact):
            print("Asking {!r}".format(fact))
            ret_list = ListOfBindings()
            for f in self.facts:
                temp = match(fact.statement, f.statement)
                if temp:
                    ret_list.add_bindings(temp)
            if len(ret_list) == 0:
                return False
            else:
                return ret_list
        else:
            print("Ask Failed: input not a Fact")
