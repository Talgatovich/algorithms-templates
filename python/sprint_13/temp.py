def get_symbols(N, M=0, prefix=None):
    if M > len(N) - 1:
        print("".join(prefix), end="  ")
        return
    prefix = prefix or []
    num = N[M]
    symbols = my_dict[num]

    for symb in symbols:
        prefix.append(symb)
        get_symbols(N, M + 1, prefix)
        prefix.pop()
