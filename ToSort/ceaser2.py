def StringChallenge(s, num):
    # Helper function to shift a single character
    def shift_char(c, shift):
        # Check if the character is a letter
        if c.isalpha():
            # Determine if it's uppercase or lowercase
            start = ord('A') if c.isupper() else ord('a')
            # Perform the shift and wrap around using modulo 26
            return chr((ord(c) - start + shift) % 26 + start)
        # If it's not a letter, return the character unchanged
        return c
    
    # Apply Caesar cipher to each character in the string
    ciphered_string = ''.join(shift_char(c, num) for c in s)
    
    # Define the ChallengeToken
    ChallengeToken = "n75zyl4h62c"
    
    # Concatenate the ciphered string with the ChallengeToken
    final_string = ciphered_string + ChallengeToken
    
    # Replace every third character with 'X'
    result = ''.join(c if (i + 1) % 3 != 0 else 'X' for i, c in enumerate(final_string))
    
    return result

# Test cases
print(StringChallenge("Hello", 4))  # Example case: Output should be "LiXpsX75XylXh6Xc"
print(StringChallenge("Caesar Cipher", 2))  # Output should be "Ecguct EkrjgtXn75zyl4h62c"
print(StringChallenge("BOB loves-coding", 3))  # Example case: Output should be "ERB oryhv-frlglqjXn75zyl4h62c"
print(StringChallenge("abc", 0))  # Example case: Output should be "ERB oryhv-frlglqjXn75zyl4h62c"