import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getBillionUsersDay(growthRates):
    # Write your code here
    #BF O(n * t) Space: O(1)
    """
      bil = 1000000000
    #1.5^t = 1000000000
    if len(growthRates) == 0:
      ans =  math.log(bil, growthRates[0])
      ans = math.ceil(ans)
      return ans
    else:
      days = 0
      users = 0
      # O(nt)
      while users < bil:
          days += 1
          users = 0
          # O(n)
          for app in growthRates:
              users = users + math.pow(app,days) 
              if users >= bil:
                  break
      return days
    """
    #using Binary search to reduce the time to O(n * log t)
    #1.1^t + 1.2^t +1.3^t = 10000000
    '''
    Time O(n log m)
    
    Space O(1)
    '''
    # O(n)
    BILLION = 1000000000
    max_rate = max(growthRates)
    # upper bound
    max_days = math.ceil(math.log(BILLION, max_rate))

    l = 1
    r = max_days
    # O(n log m)
    while l <= r:
        mid = (r + l) // 2

        users = 0
        # O(n)
        for g in growthRates:
            users += g ** mid
            if users >= BILLION:
                break

        if users < BILLION:
            l = mid + 1
        else:
            r = mid - 1

    return mid

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [1.5]
  expected_1 = 52
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)
  
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  