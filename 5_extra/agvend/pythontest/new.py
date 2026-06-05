
def get_data(val: str) -> int:
    return int(str(val)[::-1])

print(get_data("123"))
print(get_data("321"))

