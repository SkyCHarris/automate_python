# What is the difference between copy.copy() and copy.deepcopy()?

# 17. copy.deepcopy() will copy over the original list value

# Actual:
# copy.copy() will do a shallow copy of a list, while copy.deepcopy() will do a deep copy of a list.
# That is, only copy.deepcopy() will duplicate any lists inside the list