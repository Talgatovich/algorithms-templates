def sequense(line_1, line_2):
    start = -1
    for word in line_1:
        start = line_2.find(word, start + 1)
        if start == -1:
            return False
    return True

            

def read_input():
    s = input()
    t = input()
    return s, t


def main():
    s, t = read_input()
    print(sequense(s, t))


#if __name__ == "__main__":
#    main()




list1 = 'abcp'
list2 = 'ahpc'
print(sequense(list1, list2))
