def is_match(fingerprint_a, fingerprint_b):

    if len(fingerprint_a) != len(fingerprint_b):
        return False

    diferencias = sum(1 for a, b in zip(fingerprint_a, fingerprint_b) if a != b)

    print(diferencias <= len(fingerprint_a) * 0.1)

    return diferencias <= len(fingerprint_a) * 0.1

## Tests:
is_match("helloworld", "helloworld") #should return True.
is_match("helloworld", "helloworlds") #should return False.
is_match("helloworld", "jelloworld") #should return True.
is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") #should return True.
is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") #should return True.
is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") #should return False.