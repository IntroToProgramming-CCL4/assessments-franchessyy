#this will print the definition of each words written below but with other variables included
glossary = {
  'comment': 'It is used to explain or add notes to the code.',
    'set': 'A set is an unsorted collection of distinct components.',
   'list': 'A grouping of elements in a specific order.',
    'loop': 'Work through a selection of things one by one.',
    'dictionary': "A dictionary is a predefined data type that represents a set of key-value pairs.",
    'string': ', it is used to represent text data in a program They can have letters, numbers, symbols, and even spaces in them.',
    'tuple': 'Tuples are similar to lists in that their elements cannot be changed after they are created.',
    'integer': 'A data type that does not use a decimal point to represent whole numbers.',
    'float': 'A data type that uses decimal points to represent numbers.',
    'boolean expression': 'A data type that can only represent True or False. It is employed in logical operations.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)