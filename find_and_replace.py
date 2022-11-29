def find_and_replace(text, old_text, new_text) -> str:
    # If no instance of old_text is found in text return None
    if not (old_text in text):
        return f'No instance of "{old_text}" found in "{text}"'

    # Create new list containing "text"
    lText = [''] * (len(text))
    for i in range(len(text)):
        lText[i] = text[i]

    # Verify if elements of "old_text" are in the new list "lText" and get start index of "old_text" in "text"
    for i in range(len(lText)):
        verified = True

        # Check if characters are equal to the first char of old_text
        if lText[i] == old_text[0]:

            # Iterate through lText for len(old_text) times;
            # if the 2nd condition returns false then text does not contain old_text (set verified to false),
            # else get the current value of index "i" and store it in start_index
            for j in range(len(old_text)):
                if not verified: break

                if not (lText[i + j] == old_text[j]):
                    verified = False
            if verified:
                start_index = i
                break

    # Define an empty list which size is equal to the number of elements needed by the new string
    lText = [''] * (len(text) - len(old_text) + len(new_text))

    """
    # Insert original chars until start_index
    for i in range(start_index):
        lText[i] = text[i]

    # Add new chars
    for i in range(len(new_text)):
        lText[start_index + i] = new_text[i]

    # Insert remaining chars
    for i in range(len(lText) - start_index - len(new_text)):
        lText[start_index + len(new_text) + i] = text[start_index + len(old_text) + i]
    """

    for i in range(len(lText)):
        if i < start_index:
            lText[i] = text[i]
        elif i >= start_index and i < start_index + len(new_text):
            lText[i] = new_text[i - start_index]
        else:
            lText[i] = text[i - start_index]

    return ''.join(lText)
