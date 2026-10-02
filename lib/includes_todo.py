def includes_todo(string):
    if '#TODO' in string.upper():
        return True
    else:
        return False