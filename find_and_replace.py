
def find_and_replace(text, old_text, new_text):
    # If no instance of old_text is found in text return None
    if not (old_text in text):
        return None
    return text.replace(old_text, new_text)

