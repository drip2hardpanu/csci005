# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.
#
# For another example of such a file, see
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
# Name:
#

#
# First, some helper/example functions for files + text ...
#
# To make the examples work, you should have the text file named "a.txt"
# in the same directory as this .py file!
#
# If you _don't_ have "a.txt", create it.  Here are its contents:
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!
"""

import random


def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    # We assume the "utf-8" encoding, which accepts more characters than plain ASCII
    #
    # Other common codings welcome, e.g., utf-16 or latin1
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #
    f = open(filename, encoding = 'utf-8')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string    # See https://docs.python.org/3/library/string.html
                 # Note: str is different: docs.python.org/3/library/stdtypes.html#textseq

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...




"""
[a] What was in the file you analyzed?   -->    The emancipation proclamation
    + Feel free to include it (up to you).

[b] How many words did it have?  -->     724
    Use word_count.

[c] How many characters did it have?  -->       3524 (without spaces)

    Note: there's no function for this, but len(get_text("a.txt")) will do it!


[d] How many _distinct_ words did it have?  -->       266
    Use vocab_count.
    Adapt as you see fit...

[e] What are three words that appeared unusually often for this text?  --> united, states (but not america), thereof
    - ...relative to a generic distribution of "all text"

    For example, it's _not_ unusual if "the" or "a" are the
    most common words in an English text.


[f] Other thoughts/insights?!

really interesting that united and states shows up a lot but america only shows up twide

"""

#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your 500-word "CS-Essay,"" with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)       # Then copy the "essay" below ...
#

#
# Function #1  (createDictionary)
#
def createDictionary(text):
    """creates a dictionary given text...
    """
    LoW = text.split()
    d = {}
    pw = '$'

    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]
        
        pw = nw
        
        if pw[-1] == '.' or pw[-1]== '!' or pw[-1] == '?':
            pw = '$'
    # Here, check for whether that new previous word, pw, ends in 



    return d

    # punctuation -- if it _does_ then set pw to be '$'
    # that way, it will be back at the start of a new sentence!



#
# Function #2   (generateText)
#
def generateText(d, N):
    """takes in argument (dictionary, length), utilized the dictionary to generate text that is N words long...
    """
    print()  # start by printing a newline

    next_word = "poptarts"  
    previous_word = ""

    for i in range(N):

        if i == 0: #this will be for the first caste
            next_word = random.choice(d['$'])
        elif next_word[-1] in '.!?': #this will be for the second case
            next_word = random.choice(d['$'])
        else: #this will be for the last case
            previous_word = next_word
            next_word = random.choice(d[previous_word])

        # Here's how to print so that things don't always start on the next line
        # Using end = ' ' stops it going to the next line
        print(next_word, end = ' ')

    print()                  # Final print, newline


#
# Your 500-or-so-word "CS Essay" (paste into the triple-quoted strings below):
#
"""
Emancipation Proclamation: Abe Lincoln

"That on the City of Washington, this day of such persons of Washington, this first day in any State, or designated as slaves within said persons. By the United States, including the Constitution, upon the freedom of the cities of our Lord one thousand eight hundred and the Executive government of States and caused the people thereof, respectively, are this first day in necessary war measure for their actual freedom. Whereas, on that any efforts they may make known, that the people thereof, shall be free to wit: Arkansas, Texas, Louisiana, (except the President of said designated as West Virginia, and as the Constitution, upon this proclamation was issued by members chosen thereto at elections wherein the power in the following, to garrison forts, positions, stations, and parts of Almighty God. And upon the United States; and parts of States, containing, among other places, and parts of said persons. Mary, St. James Ascension, Assumption, Terrebonne, Lafourche, St. James Ascension, Assumption, Terrebonne, Lafourche, St. Martin, and naval authority thereof, will recognize and which excepted parts, are not then in time of Norfolk and Orleans, including the Army and to repress such State or acts to abstain from the forty-eight counties of our Lord one thousand eight hundred and maintain the power in rebellion against the military necessity, I recommend to garrison forts, positions, stations, and Portsmouth[)], and maintain the Constitution, upon the freedom of State. James Ascension, Assumption, Terrebonne, Lafourche, St. By the United States." Now, therefore I, Abraham Lincoln, President of the twenty-second day of justice, warranted by the United States." Now, therefore I, Abraham Lincoln, President of the States in rebellion against the United States, including the people thereof, are this proclamation was issued by virtue of States, the following, to them that, in the following, to do no act or acts to garrison forts, positions, stations, and sixty-three, and which the present, left precisely as a State, or designated part of States, shall be then, thenceforward, and sixty-three, and which the United States, shall be an act of them, in rebellion against the President of our Lord one thousand eight hundred and Portsmouth[)], and the armed service of January, in good faith, represented in the first day of the United States wherein the year of such persons, or the full period of the freedom of Norfolk and parts of the States and for their actual armed service of the military and make known, that such State or acts to be received into the United States." Now, therefore I, Abraham Lincoln, President of America the United States; and for the first day of the States and necessary self-defence; and Virginia, and Norfolk, including the year of America: A Transcription By the people thereof respectively, are this act, sincerely believed to repress such persons, or designated part of the United States." Now, therefore I, Abraham Lincoln, President of States, if this day of the President of them, in all sorts in the City of the United States to garrison forts, 


"""
