# LeetCode 288 - Unique Word Abbreviation

## Problem Statement

An abbreviation of a word is created using the following rules:

* If the word has more than 2 characters, keep the first and last characters.
* Replace the characters between them with the number of characters removed.

For example:

```text
internationalization → i18n
apple → a3e
dog → d1g
```

Given a dictionary of words, determine whether the abbreviation of a given word is unique.

A word's abbreviation is considered unique if:

1. The abbreviation does not belong to any word in the dictionary, or
2. The only word in the dictionary with that abbreviation is the same word.

---

## Example

### Input

```text
dictionary = ["deer", "door", "cake", "card"]
word = "dear"
```

### Abbreviations

```text
deer → d2r
door → d2r
cake → c2e
card → c2d
dear → d2r
```

Since both `deer` and `door` have the abbreviation `d2r`, the abbreviation of `dear` is not unique.

### Output

```text
False
```

---

## Another Example

```text
dictionary = ["deer", "door", "cake", "card"]
word = "cart"
```

The abbreviation is:

```text
cart → c2t
```

No word in the dictionary has the abbreviation `c2t`.

Therefore:

```text
Output:
True
```

---

## Approach

We use a **Hash Map** and **Set**.

For every word in the dictionary:

1. Calculate its abbreviation.
2. Store the word inside a set associated with that abbreviation.

For example:

```text
deer → d2r
door → d2r
```

The hash map becomes:

```text
d2r → {"deer", "door"}
```

When checking a word:

1. Calculate its abbreviation.
2. If the abbreviation is not in the map, the word is unique.
3. If the abbreviation exists:

   * It is unique only if the set contains exactly the same word.

---

## Algorithm

### Constructor

1. Store all dictionary words in a set.
2. Traverse every word in the dictionary.
3. Generate its abbreviation.
4. Store the word in the set corresponding to that abbreviation.

### `isUnique(word)`

1. Generate the abbreviation of `word`.
2. Check whether the abbreviation exists in the hash map.
3. If it does not exist, return `True`.
4. If it exists and its set contains only `word`, return `True`.
5. Otherwise, return `False`.

---

## Abbreviation Rules

For a word with more than two characters:

```text
first character + number of middle characters + last character
```

Examples:

```text
apple  → a3e
hello  → h3o
leetcode → l6e
```

For words with one or two characters, the word itself is used.

Examples:

```text
a  → a
it → it
```

---

## Example Walkthrough

Dictionary:

```text
["deer", "door", "cake", "card"]
```

The abbreviations are:

```text
deer → d2r
door → d2r
cake → c2e
card → c2d
```

Check:

```text
word = "dear"
```

Abbreviation:

```text
dear → d2r
```

The abbreviation `d2r` belongs to:

```text
{"deer", "door"}
```

It does not uniquely identify `dear`.

Therefore:

```text
False
```

---

## Why This Works

The hash map groups words according to their abbreviations.

If an abbreviation belongs to multiple different words, it cannot uniquely identify any one of those words.

If it belongs only to the word being checked, the abbreviation is unique.

---

## Time Complexity

Let `N` be the number of words in the dictionary and `L` be the average word length.

Creating all abbreviations takes:

**Time Complexity:** `O(N × L)`

Checking a word takes:

**O(L)**

---

## Space Complexity

The hash map stores the abbreviations and dictionary words.

**Space Complexity:** `O(N × L)`

---

## Key Concept

The main concepts used are:

* Hash Map
* Hash Set
* String manipulation
* Abbreviation
* Dictionary lookup

---

## Language

Python

## LeetCode Problem

288 - Unique Word Abbreviation

## Author

T. Nandhini
