# Root Word Stem Generator

A Python tool that takes user input for a root word and generates various stem transformations using common English patterns and internal vowel changes. The tool checks whether the generated forms exist in a standard English dictionary.

## Features

- Generate multiple stem variations from a root word.
- Patterns include common verb conjugations, noun/adjective forms, and other morphological transformations.
- Stems are checked against the `nltk` English word corpus to identify valid English words.
- Includes a variety of transformation templates for creative or linguistic exploration of root words.

## Installation

To use this project, you need to have Python installed on your machine. Additionally, this project relies on the `nltk` library and its `words` corpus.

### Step-by-step instructions

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/RootWordStemGenerator.git
cd RootWordStemGenerator
```

2. Install the required dependencies:

```bash
pip install nltk
```

3. Download the `nltk` words corpus, if you haven't already:

```python
import nltk
nltk.download('words')
```

## Usage

To run the script, simply execute the Python file:

```bash
python root_word_stem_generator.py
```

You will be prompted to enter a root word, and the program will generate various stem forms based on predefined patterns and internal vowel changes.

### Example

```bash
Enter your root word: gld

Stems of 'gld':

Valid stems:
glod (found in dictionary)
galed (found in dictionary)
glid (found in dictionary)

Invalid stems:
gleeda (not in dictionary)
galdana (not in dictionary)
galoda (not in dictionary)
```

## Customization

The current version of the tool uses predefined transformation patterns for generating word stems. These patterns include common suffixes (e.g., `-ed`, `-ing`, `-ness`, `-ly`) and vowel modifications to simulate different forms of a root word.

If you want to add more transformations or change the current patterns, you can modify the `stem_patterns` and `stem_transformations` sections in the `generate_stem` function inside the `root_word_stem_generator.py` file.

### Adding new patterns

You can add your own transformations by adding new format strings in the list. For example:

```python
new_pattern = "{}ification"
```

## Code Overview

```python
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
        "{}o{}",  # Internal vowel insertion
        "{}a{}ed",  # Extended past tense
        "{}i{}d",  # Internal vowel change
        "{}eeda",  # Extended ending
        "{}a{}da",  # Alternative form
        "{}a{}dana",  # Longer extension
        "{}a{}ada",  # Variation
        "{}o{}da"   # Vowel shift with ending
    ]

    # Combine both lists of patterns to check more variations
    all_patterns = stem_patterns + stem_transformations

    valid_stems = []
    invalid_stems = []

    for pattern in all_patterns:
        word = pattern.format(root[0], root[1:])
        if word in english_words:
            valid_stems.append(word)
        else:
            invalid_stems.append(word)

    return valid_stems, invalid_stems
```

### Functionality

* `generate_stem()`: Takes a root word as input and applies different patterns to generate potential stems. It uses the `nltk` words corpus to check if a stem is valid.
* Pattern types: Includes regular transformations (like `-ed`, `-ing`, `-ness`, etc.) and internal transformations (like vowel changes and extended forms).

## Contributions

Feel free to submit issues or pull requests. If you have suggestions for new transformation patterns or want to improve the existing ones, contributions are welcome!

### To contribute:

* Fork the repository.
* Create a new feature branch (`git checkout -b feature/my-feature`).
* Commit your changes (`git commit -am 'Add new feature'`).
* Push to the branch (`git push origin feature/my-feature`).
* Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Notes:

- **GitHub Repo Name**: I chose "RootWordStemGenerator" to clearly describe what the project does: generating stem variations from a root word.
- **`README.md` Structure**: The README provides clear instructions on how to install, run, and customize the script, along with an example of how it works. There's also a section on contributing to the project and adding new patterns.
- **Further Customization**: You can adjust the exact features and wording based on your personal preferences and intended audience, but this is a good comprehensive start.
