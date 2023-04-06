#!/usr/bin/python3
"""Defines a function that prints 2 new lines 
after certain characters"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters ., ? and :
    """
    # Check if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Remove any leading or trailing whitespace
    text = text.strip()
    
    # Initialize the result string
    result = ""
    
    # Loop over each character in the text
    for i in range(len(text)):
        # Append the current character to the result string
        result += text[i]
        
        # Check if the current character is one of ., ? or :
        if text[i] in (".", "?", ":"):
            # Add 2 new lines after the character
            result += "\n\n"
    
    # Print the result string
    print(result)

