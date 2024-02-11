def is_subset(set_a, set_b):
    return set_a.issubset(set_b)


def is_subset_variant_two(set_a, set_b):
    return set_a <= set_b


setA = {1, 2, 3, 4, 5}
setB = {2, 3, 4}
setC = {4, 5}
setD = {2, 3, 4}

print(f"setA <= setB {is_subset(setA, setB)}")
print(f"setB <= setA {is_subset(setB, setA)}")
print(f"setC <= setA {is_subset(setC, setA)}")
print(f"setD <= setB {is_subset(setD, setB)}")

print("--------------------")

print(is_subset_variant_two(setA, setB))
print(is_subset_variant_two(setB, setA))
print(is_subset_variant_two(setC, setA))
print(is_subset_variant_two(setD, setB))