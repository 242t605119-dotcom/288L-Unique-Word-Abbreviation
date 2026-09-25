class ValidWordAbbr:

    def __init__(self, dictionary):
        self.words = set(dictionary)
        self.abbreviations = {}

        for word in dictionary:
            if len(word) <= 2:
                abbr = word
            else:
                abbr = word[0] + str(len(word) - 2) + word[-1]

            if abbr not in self.abbreviations:
                self.abbreviations[abbr] = set()

            self.abbreviations[abbr].add(word)

    def isUnique(self, word):
        if len(word) <= 2:
            abbr = word
        else:
            abbr = word[0] + str(len(word) - 2) + word[-1]

        if abbr not in self.abbreviations:
            return True

        return self.abbreviations[abbr] == {word}
