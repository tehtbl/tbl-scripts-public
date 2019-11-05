#!/usr/bin/env python3

import os
import sys
import random

from optparse import OptionParser

import pprint
pp = pprint.PrettyPrinter(indent=4)

#
# MAiN
#
if __name__ == "__main__":

    #usage = "usage: %prog [options]"
    #parser = OptionParser(usage=usage)
    
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="infile", type="string", help="input FILE to use (dictionary)", metavar="FILE")
    parser.add_option("-l", "--len", dest="word_len", type="int", help="len of words to choose", default=4, metavar="INT")
    parser.add_option("-n", "--amount", dest="amount", type="int", help="how much to choose", default=20, metavar="INT")
    parser.add_option("-w", "--word", dest="word", help="word to combine", default="mail", metavar="WORD")
    parser.add_option("-a", "--attach", action="store_true", dest="mod_attach", default=False, help="attach to word")
    parser.add_option("-p", "--pre", action="store_true", dest="mod_pre", default=False, help="before word")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="be verbose")

    (options, args) = parser.parse_args()

    word_ll = []
    try:
        word_ll = [i.replace('\n', '') for i in open(options.infile, 'r').readlines()]
    except:
        print("use a valid dictionary file!")
        os._exit(-1)

    w_len = int(options.word_len)
    if not w_len > 1:
        print("use a len > 1")
        os._exit(-1)

    word = options.word
    if not len(word) > 1:
        print("use a word len > 1")
        os._exit(-1)

    if options.verbose:
        print("="*80)
        print("config:")
        print("  dict file: '{}', size: {}".format(options.infile, len(word_ll)))
        print("  word len: {}".format(w_len))
        print("  my word: '{}'".format(word))
        print("  attaching? {}".format(options.mod_attach))
        print("  pre? {}".format(options.mod_pre))
        print("  how much? {}".format(options.amount))
        print("="*80)
        print("")

    word_ll_len = [w.lower() for w in word_ll if len(w) is w_len]
    rnd_words = random.choices(word_ll_len, k=options.amount)
    
    final_words = []
    for w in rnd_words:
        new_word = ""

        if options.mod_attach:
            new_word = "{}{}".format(word, w)
        elif options.mod_pre:
            new_word = "{}{}".format(w, word)
        else:
            new_word = "{}{}".format(w, word)
        
        final_words.append(new_word)

    n = 7
    final_print = [final_words[i:i + n] for i in range(0, len(final_words), n)]

    print("-"*3)
    for line in final_print:
        print("   ".join(line))
    print("-"*3)

