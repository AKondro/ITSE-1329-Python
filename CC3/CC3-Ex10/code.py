# Without adding any new code, make count_at_symbols work as intended
def count_at_symbols(phrase):
    count = 0
    for char in phrase:
        if char == '@':
            count = + 1
        return count

