import random, string, sys
from collections import Counter, defaultdict

### Fill in each function below.

### Run "python -m doctest 2_words.py" at the command line to test your work.

def word_counts(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary whose keys are all the words in the file (broken by
    whitespace). The value for each word is a dictionary containing each word
    that can follow the key and a count for the number of times it follows it.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Example:
    >>> #example.txt is a file containing: "The cat chased the dog"
    >>> with open('example.txt') as f:
    ...     word_counts(f)
    {'the': {'dog': 1, 'cat': 1}, 'chased': {'the': 1}, 'cat': {'chased': 1}}
    '''

    raw_word_list = [word.lower().strip() for word in f.read().split()]
    fc = map(lambda x: x.translate(string.maketrans("",""), string.punctuation), raw_word_list)

    word_dic = defaultdict(list)

    for i, item in enumerate(fc):
        if i < len(fc) - 1:
            word_dic[item].append(i)

    return {key: dict(Counter([fc[value[v]+1] for v in xrange(len(value))])) for key, value in word_dic.items()}


def associated_words(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of two consecutive words in
    the file and the value for each key is a list of words that were found
    directly following the key.

    Words should be included in the list the number of times they appear.

    Example:
    >>> with open('alice.txt') as f:
    ...     d = associated_words(f)
    >>> d[('among', 'the')]
    ['people', 'party.', 'trees,', 'distant', 'leaves,', 'trees', 'branches,', 'bright']
    '''
    fc = []
    for line in f:
        map(lambda x: fc.append(x.strip()), line.split())

    word_dic = defaultdict(list)

    for i in xrange(len(fc)-2):
        word_dic[(fc[i], fc[i+1])].append(fc[i+2])

    return word_dic


def make_random_story(f, num_words):
    '''
    INPUT: file, integer
    OUTPUT: string

    Call associated_words on file f and use the resulting dictionary to
    randomly generate text with num_words total words.

    Choose the next word by using random.choice to pick a word from the list
    of possibilities given the last two words.

    Use join method to turn a list of words into a string.

    Example:
    >>> # Seed the random number generator for consistent results
    >>> random.seed('Is the looking-glass is half full or half-empty?')
    >>> # Generate a random story
    >>> with open('alice.txt') as f:
    ...     story = make_random_story(f, 10)
    ...     story  # Note: your random story may not match this example
    stick, and tumbled head over heels in its sleep 'twinkle,
    >>> len(story.split())  # Verify story length is 10 words
    10
    '''
    word_dic = associated_words( f )
    random.seed('I love word dictionary')
    random_story = list(random.choice(word_dic.keys()))

    for i in xrange(num_words - 2):
        first_two = tuple([random_story[len(random_story) - 2], random_story[len(random_story) - 1]])
        new_word = random.choice(word_dic[first_two])
        random_story.append(new_word)

    return " ".join(random_story)


if __name__ == '__main__':
    # This code will be run if you on the command line run: python words.py
    if len(sys.argv) >= 3 and sys.argv[2].isdigit():
#        with open('alice.txt') as f:
        with open(sys.argv[1]) as f:
#           print make_random_story(f, 100)
            print make_random_story(f, int(sys.argv[2]))
