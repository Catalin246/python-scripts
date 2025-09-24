def sum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if i != j:
                s = array[i] + array[j]
                if s == target:
                    return [i, j]          
    return [-1, -1]

# Test cases: (array, target, expected)
tests = [
    ([1, 3, 2, 4], 5, [0, 3]),       
    ([-2, -1, 3, 5], 2, [1, 2]),     
    ([1, 2, 3], 10, [-1, -1]),       
    ([3, 3, 4], 6, [0, 1]),          
    ([5], 5, [-1, -1])               
]

# Run tests
for i, (array, target, expected) in enumerate(tests, start=1):
    result = sum(array, target)
    passed = result == expected
    print(f"Test {i}: array={array}, target={target}")
    print(f"Expected: {expected}, Got: {result}  {'PASS' if passed else 'FAIL'}\n")

def all_pairs(array, target):
    pairs = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)): 
            if array[i] + array[j] == target:
                pairs.append([i, j])
    return pairs if pairs else [[-1, -1]]