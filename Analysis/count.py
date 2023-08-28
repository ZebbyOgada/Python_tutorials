# This code counts the number of occurenecs (m) in (tot)

def count(tot, m):
    count = 0

    for element in tot:
        if element == m:
            count += 1
    return count

#Test cases

test_cases = [([1,1,3,5,7,7,8,2,2,5],1),("peaky pecky","p")]
for test_case in test_cases:
    print("Test case :{},{}".format(test_case[0],test_case[1]))
    print("Result :{}\n".format(count(test_case[0],test_case[1])))
