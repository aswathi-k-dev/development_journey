def ransom_note(note,magazine):
    for char in note:
        if char  not in magazine:
            print(False)
            break
    else:
        print(True)
ransom_note("hen","chicken")
ransom_note("pen","chicken")
ransom_note("pen","pencil")