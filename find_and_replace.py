def find_and_replace(text, old_text, new_text) -> str:
    # If no instance of old_text is found in text return None
    if not (old_text in text):
        return f'No instance of "{old_text}" found in "{text}"'

    # Create new list containing "text"
    lText = [''] * (len(text))
    for i in range(len(text)):
        lText[i] = text[i]

    # Verify if elements of "old_text" are in the new list "lText" and get start index of "old_text" in "text"
    i: int = 0
    verified = False
    start_index = None
    while i < len(lText) and not verified:
        # Check if char[i] of lText is equal to the first char of old_text
        if lText[i] == old_text[0]:

            # check if list of chars are equal
            if lText[i:i+len(old_text)] == list(old_text):
                verified = True
                start_index = i
        i += 1

    if not verified:
        return f'Error: couldn\'t get start_index '

    # Define an empty list which size is equal to the number of elements needed by the new string
    lText = [''] * (len(text) - len(old_text) + len(new_text))

    # Insert original chars until start_index
    for i in range(start_index):
        lText[i] = text[i]

    # Add new chars
    for i in range(len(new_text)):
        lText[start_index + i] = new_text[i]

    # Insert remaining chars
    for i in range(len(lText) - start_index - len(new_text)):
        lText[start_index + len(new_text) + i] = text[start_index + len(old_text) + i]

    return ''.join(lText)
