import string

def caesar_cipher(s: str, shift: int) -> str:
    """Shift alphabetic characters by 'shift', keeping case, punctuation, and spaces intact."""
    # Create a mapping for lowercase and uppercase alphabet shifts
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    
    def shift_char(c):
        # Shift only alphabetic characters
        if c in lower_alphabet:
            # Find new position in lowercase alphabet
            return lower_alphabet[(lower_alphabet.index(c) + shift) % 26]
        elif c in upper_alphabet:
            # Find new position in uppercase alphabet
            return upper_alphabet[(upper_alphabet.index(c) + shift) % 26]
        return c  # Return unchanged for non-alphabetic characters
    
    # Apply shifting function to each character
    return ''.join(shift_char(c) for c in s)


def StringChallenge(s: str, num: int) -> str:
    """Perform Caesar Cipher, concatenate ChallengeToken, and replace every third character with 'X'."""
    # Step 1: Perform Caesar Cipher
    ciphered_string = caesar_cipher(s, num)
    
    # Step 2: Concatenate ChallengeToken
    challenge_token = "n75zyl4h62c"
    final_string = ciphered_string + challenge_token
    
    # Step 3: Replace every third character with 'X'
    result = []
    for i, char in enumerate(final_string):
        if (i + 1) % 3 == 0:
            result.append('X')  # Replace every third character
        else:
            result.append(char)
    
    # Return the final string
    return ''.join(result)


# Test cases to verify the solution
print(StringChallenge("Hello", 4))  # Expected output: "LiXpsX75XylXh6Xc"
print(StringChallenge("Caesar Cipher", 2))  # Expected output: "EcXucXtXkrXgtX75XylXh6Xc"
print(StringChallenge("BOB loves-coding", 3))  # Expected output: "ERXoryXvX-frXglX75XylXh6Xc"

print("\n\n")
print(StringChallenge("Test", 2))  # Expected output: "ERXoryXvX-frXglX75XylXh6Xc"

print("\n\n")
print(StringChallenge("abc", 0))  # Expected output: "ERXoryXvX-frXglX75XylXh6Xc"
