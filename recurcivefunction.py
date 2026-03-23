#function that calls itself
nested = [1,[2,[3,4],5],6,[7,8]]
def flatten(nested):
    flat_list = []
    for num in nested:
        if isinstance(num, list):
            flat_list.extend(flatten(num))
        else:
            flat_list.append(num)
    return flat_list
print(flatten(nested))
