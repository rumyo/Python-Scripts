# Practicando con python

String Reference Cheat Sheet

In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.

String operations

   - len(string) Returns the length of the string
   - for character in string Iterates over each character in the string
   - if substring in string Checks whether the substring is part of the string
   - string[i] Accesses the character at index i of the string, starting at zero
   - string[i:j] Accesses the substring starting at index i, ending at index j-1. 
   - If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

String methods

   - string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
   - string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
   - string.count(substring) Returns the number of times substring is present in the string
   - string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
   - string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
   - string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
   - string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
   - delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 

Check out the official documentation for all available String methods: https://docs.python.org/3/library/stdtypes.html#string-methods


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary Methods Cheat Sheet

Definition

x = {key1:value1, key2:value2}

Operations

   - len(dictionary) - Returns the number of items in the dictionary
   - for key in dictionary - Iterates over each key in the dictionary
   - for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
   - if key in dictionary - Checks whether the key is in the dictionary
   - dictionary[key] - Accesses the item with key key of the dictionary
   - dictionary[key] = value - Sets the value associated with key
   - del dictionary[key] - Removes the item with key key from the dictionary

Methods

   - dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
   - dict.keys() - Returns a sequence containing the keys in the dictionary
   - dict.values() - Returns a sequence containing the values in the dictionary
   - dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
   - dict.clear() - Removes all the items of the dictionary
    
   official documentation: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
   
   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
   # Bash scripting cheatsheet
   
   https://devhints.io/bash
   
   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
