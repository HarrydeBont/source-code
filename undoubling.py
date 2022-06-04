# Strip de name to the core ignopring the double underscore indicating multiple face as input of one person

def undouble(name):
    """
    Undoubles multiple images encoding the same person.
    Multiple image for the same person can be coded (in the filename) with double underscore followed by a number

    """
    double = name.find("__")
    if (double>0):
        undoubled_name = name[:double]
    else:
        undoubled_name = name
    return(undoubled_name)
