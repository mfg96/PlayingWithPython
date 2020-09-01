# Muhammad Faraz Sohail


# method countVowels to count the number of vowels in the given string
def countVowels(sent):
    upper = str.upper(sent)  # converting string to upper case letters
    sList = list(upper)  # making lis of every character in the string
    # then we counted each character of vowel in the given string below
    a = sList.count('A')
    e = sList.count('E')
    i = sList.count('I')
    o = sList.count('O')
    u = sList.count('U')
    totalCount = a+e+i+o+u  # adding total count of vowels
    return totalCount  # returning total count


# string to be used
string = "Jingle bells, jingle bells Jingle all the way Oh! what fun it is to ride In a one horse open sleigh, hey JINGLE BELLS, JINGLE BELLS Jingle all the way"

# calling the method countVowels and printing the results
print('Total vowels int the string are = ', countVowels(string))


# method to produce results
def pToD(inp):
    p = inp  # assigning p the input value
    # stripping of percent sign if any and then diving by 100
    decimal = float(p.strip('%'))/100
    print("Equivalent Decimal", decimal)  # printing the results


inp = input("Enter Percentage: ")  # taking input
pToD(inp)  # calling method
