#this will print out the definition of each words written below

glossary = {
    'comment': 'It is used to explain or add notes to the code.',
    'set': 'A set is an unsorted collection of distinct components.',
    'list': 'A grouping of elements in a specific order.',
    'loop': 'Work through a selection of things one by one.',
    'dictionary': "A dictionary is a predefined data type that represents a set of key-value pairs.",
    }

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'set'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])