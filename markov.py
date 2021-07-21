"""Generate Markov text from text files."""
import sys 

argv = sys.argv 

#import random choice
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    #open the file and assign it to "file"
    file = open("green-eggs.txt")

    #read the file & assign to a variable
    full_green_eggs = file.read()

    #get rid of whitespace in the text file & assign to "words" variable
    words = full_green_eggs.split()

    # print(words)

    return words


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    

    full_text = open_and_read_file("green-eggs.txt")

    for i in range(len(full_text) - 2):
        my_tuple = (full_text[i], full_text[i + 1])
        # print(my_tuple)
        values = []
        chains[my_tuple] = full_text[i + 2]

        # if my_tuple in chains.keys():
        #     print(my_tuple)

        #check if the key is in the dictionary
            #if not, create an empty list
            #then append the value to the empty list 
            #if yes, append the value to the existing list

    #  = values.append(my_tuple)

    # print(chains)
        # return


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

#current_key = chain.split()
#chosen_word = random.choice(chains[current_key])
#new-key = (current_key[1], chosen_word)
    

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
