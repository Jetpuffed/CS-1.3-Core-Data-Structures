#!usr/bin/env python3


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    if pattern in text:
        return True
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    if contains(text, pattern):
        return text.index(pattern)
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    return [i for i, v in enumerate(text) if text.startswith(pattern, i)]


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print("contains({!r}, {!r}) => {}".format(text, pattern, found))
    index = find_index(text, pattern)
    print("find_index({!r}, {!r}) => {}".format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print("find_all_indexes({!r}, {!r}) => {}".format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print("Usage: {} text pattern".format(script))
        print("Searches for occurrences of pattern in text")
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == "__main__":
    main()
