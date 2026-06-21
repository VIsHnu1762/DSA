# Python3 Program to implement
# the above approach

# Function to obtain lexicographically
# smallest string possible by inserting
# character c in the string s
def SmallestString(s, c):

    i = 0

    # Traverse the string
    while(i < len(s)):

      # Check if current character is
      # greater than the given character
        if s[i] > c:

            # Insert the character before
            # the first greater character
            s = s[:i] + c + s[i:]

            # Return the string
            return s
        i = i + 1

    # Append the character at the end
    s = s + c

    # Return the string
    return s


S = 'abd'
C = 'c'

# Function call
print(SmallestString(S, C))