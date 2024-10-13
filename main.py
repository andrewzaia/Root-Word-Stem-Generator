import nltk
from nltk.corpus import words

# Download the NLTK words corpus if not already available
nltk.download('words')

def generate_stem(root):
    # Fetch all English words from nltk corpus
    english_words = set(words.words())

    # Define a variety of possible stem patterns
    stem_patterns = [
        "{}ed",      # Past tense
        "{}ing",     # Present participle
        "{}s",       # Plural or third-person singular present
        "{}er",      # Comparative or agent noun
        "{}est",     # Superlative
        "{}ly",      # Adverbial form
        "{}ment",    # Noun from verb
        "{}ness",    # Noun form from adjective
        "{}ful",     # Adjective form with 'full'
        "{}less",    # Adjective form with 'less'
        "{}ation",   # Noun form from verbs
        "{}ify",     # Verb form
        "{}able",    # Adjective form with 'able'
        "{}ous",     # Adjective form with 'ous'
        "{}ion",     # Noun form
        "{}ize",     # Verb form
        "{}al",      # Adjective form
        "{}ist",     # Person noun form
        "{}ian",     # Professional noun form
        "{}ship",    # Noun form for states or conditions
        "{}hood",    # Noun form for conditions or relationships
    ]

    # General stem transformations like internal vowel changes and additions
    stem_transformations = [
        "{}o{}",  # G-Stem like
        "{}a{}ed",  # Extended past tense
        "{}i{}d",  # Internal vowel change
        "{}eeda",  # Alternative ending
        "{}a{}da",  # Extended ending
        "{}a{}dana",  # Longer extension
        "{}a{}ada",  # Variation
        "{}o{}da"   # Internal vowel shift with ending
    ]
    
    # Combine both lists of patterns to check more variations
    all_patterns = stem_patterns + stem_transformations

    # Apply patterns and check if the result is a valid word
    valid_stems = []
    invalid_stems = []

    print(f"\nStems of '{root}':")
    for pattern in all_patterns:
        word = pattern.format(root[0], root[1:])
        if word in english_words:
            valid_stems.append(word)
        else:
            invalid_stems.append(word)

    # Output the results
    print("\nValid stems:")
    for word in valid_stems:
        print(word)

    print("\nInvalid stems (not found in dictionary):")
    for word in invalid_stems:
        print(word)


# Ask the user for input
root = input("Enter your root word: ").strip()

# Generate the stems
generate_stem(root)
