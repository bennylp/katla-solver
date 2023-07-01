from argparse import ArgumentParser
from enum import Enum
from random import seed, randint
import sys
from typing import Dict, List

NONE = 0
MISS = 1
CORRECT = 2

RESULT_CHARS = {
    NONE: '⬜️',
    CORRECT: '🟩',
    MISS: '🟨'
}

EXCLUDE_CORRECT = 2
EXCLUDE_SEEN = 1

MAX_RETRIES = 10

with open('words.txt') as f:
    words = [w.strip() for w in f.readlines()]

letter_cnts = {}
for word in words:
    for letter in word:
        letter_cnts[letter] = letter_cnts.get(letter, 0) + 1

word_scores = {word: sum([letter_cnts[letter] for letter in set(word)]) for word in words}
word_scores = dict(sorted(word_scores.items(), key=lambda e: e[1], reverse=True))

def make_guess(answers: Dict[str, List[int]], exclude_rule = 0, max = 5):
    exclude_letters = set([])
    exact_letters: List[str] = ['' for _ in range(5)]
    known_letters = set([])

    for word, result in answers.items():
        for i in range(5):
            if result[i] >= MISS:
                known_letters.add( word[i] )
            if result[i]==NONE or exclude_rule==EXCLUDE_SEEN:
                exclude_letters.add(word[i])
            elif result[i]==CORRECT:
                if exclude_rule==EXCLUDE_CORRECT:
                    exclude_letters.add(word[i])
                else:
                    exact_letters[i] = word[i]

    possible_letters: List[List[str]] = [[] for _ in range(5)]

    for i in range(5):
        if exact_letters[i]:
            possible_letters_at_index = [exact_letters[i]]
        else:
            possible_letters_at_index = set()
            for word in word_scores.keys():
                if word[i] not in exclude_letters:
                    miss = False
                    for ans, result in answers.items():
                        if word[i]==ans[i] and result[i]==MISS:
                            miss = True
                    if not miss:
                        possible_letters_at_index.add(word[i])

        possible_letters[i] = possible_letters_at_index

    guesses = {}
    for word, value in word_scores.items():
        match = True
        kl = known_letters.copy()

        for i in range(5):
            if word[i] not in possible_letters[i]:
                match = False
                break
            if word[i] in kl:
                kl.remove(word[i])

        if match and len(kl)==0:
            guesses[word] = value

        if len(guesses) >= max:
            break

    return guesses


def play(answers):
    best_scores: Dict[str,int] = {}
    for retry, (word, results) in enumerate(answers.items()):
        for i in range(5):
            if results[i] > best_scores.get( word[i], 0):
                best_scores[ word[i] ] = results[i]
        str_results = lambda results: ''.join([RESULT_CHARS[r] for r in results])
        print(f'  {retry+1}. {word}: {str_results(results)}')

    exclude_rule = (0 if sum(best_scores.values()) >= 5 else
                    EXCLUDE_SEEN if len(answers) < 2 else 
                    0)
    guesses = make_guess(answers, exclude_rule=exclude_rule, max=50)
    if not guesses:
        #print('Setting exclude_rule = False')
        guesses = make_guess(answers, exclude_rule=0, max=50)

    print('\nSaran kata tebakan berikutnya beserta skornya:')
    for word, value in guesses.items():
        print(f'  {word} {value:5d}')


def get_results(guess: str, secret: str):
    results = []
    for i in range(5):
        if guess[i] == secret[i]:
            results.append( CORRECT )
        elif guess[i] in secret:
            results.append( MISS )
        else:
            results.append( NONE )
    return results

def simulate(secret=None, exclude_rules=[0]*MAX_RETRIES, verbosity=1):
    MAX_GUESSES = 15

    if not secret:
        secret = words[ randint(0, len(words)-1) ]

    if verbosity > 0:
        print(f'Secret word: {secret}')

    answers = {}
    for retry in range(MAX_RETRIES):
        if verbosity >= 2:
            print(f'Try {retry+1}:')

        guesses = make_guess(answers, exclude_rule=exclude_rules[retry], max=MAX_GUESSES)
        if not guesses:
            guesses = make_guess(answers, exclude_rule=0, max=MAX_GUESSES)

        if verbosity >= 2:
            print(f'  Guesses: {guesses}')

        the_guess = list(guesses.keys())[0]
        results = get_results(the_guess, secret)

        if verbosity >= 1:
            if len(guesses) >= MAX_GUESSES:
                #chance = f' <{1 / len(guesses):2.0%}'
                chance = '    '
            else:
                chance = f'{1 / len(guesses):4.0%}'
            str_results = lambda results: ''.join([RESULT_CHARS[r] for r in results])
            print(f'  {retry+1}. {the_guess} [chance:{chance}]: {str_results(results)}')

        if results==[CORRECT]*5:
            return retry+1

        answers[ the_guess ] = results

    return retry+1


def simulations(cnt, exclude_rules, verbosity=1):
    seed(100)
    retries = []
    for _ in range(cnt):
        retries.append( simulate(None, exclude_rules, verbosity=verbosity) )

    print(f'Average: {sum(retries)/len(retries):.1f}')


def main():
    parser = ArgumentParser(prog='katla solver')
    parser.add_argument('command', choices=['play', 'sim'])
    parser.add_argument('answer', nargs='*',
                        help='Format: word=score, e.g: bijak=00210, where bijak is the '
                             'word (i.e. your guess), 0=letter does not '
                             'exist, 1=letter exist but position is incorrect, '
                             '2=letter and position is correct')
    parser.add_argument('-c', '--count', type=int, default=10,
                        help='Simulation count')
    parser.add_argument('--verbosity', type=int, default=1)

    args = parser.parse_args()

    if args.command == 'play':
        answers = {}
        for arg in args.answer:
            tokens = arg.split('=')
            if len(tokens) != 2 or len(tokens[1])!=5:
                parser.usage()
                sys.exit(1)
            word = tokens[0]
            result = [int(c) if int(c)<=2 else 2 for c in tokens[1]]
            answers[word] = result
    
        play(answers)

    elif args.command == 'sim':
        exclude_rules = [EXCLUDE_SEEN, EXCLUDE_SEEN] + [0]*(MAX_RETRIES-2)
        simulations(args.count, exclude_rules=exclude_rules, verbosity=args.verbosity)


if __name__ == '__main__':
    main()
