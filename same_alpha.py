# q2 =try to perform a reduce operation to get a count of all the word starting with same alphabet

test_str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...'

print("The original string is : " + str(test_str))

letter = "l"


res = len(list(filter(lambda ele: letter in ele, test_str.split())))

print("Words count : " + str(res))
