# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.

def addtion(thingy):
    sum = 0
    for val in thingy.values():
        if(type(val) == int):
            sum += val
    return sum
exp = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

print(addtion(exp))