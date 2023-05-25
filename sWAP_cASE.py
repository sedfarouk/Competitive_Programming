def swap_case(s):
    return ''.join([i.upper() if i.islower() else i.lower() for i in s])

print(swap_case("HeLlo WorLD"))