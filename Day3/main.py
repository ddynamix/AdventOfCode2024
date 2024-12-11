import re

to_match = "(mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don\\'t\\(\\))"
muls_list = []

if __name__ == '__main__':
    # get the uncorrupted segments
    f = open("input.txt", "r")
    for line in f:
        muls = re.findall(to_match, line)
        muls_list = muls_list + muls

    # multiply and add the correct numbers
    products = []
    enabled = True

    print(muls_list)

    for mult in muls_list:
        if mult[0:3] == "mul" and enabled:
            comma_index = mult.index(',')
            paren1_index = mult.index('(')
            paren2_index = mult.index(')')

            term1 = mult[paren1_index + 1:comma_index]
            term2 = mult[comma_index + 1:paren2_index]

            product = int(term1) * int(term2)
            products.append(product)
        else:
            if mult == "do()":
                enabled = True
            elif mult == "don't()":
                enabled = False
            else:
                print("Erorrrrr")

    print(sum(products))
