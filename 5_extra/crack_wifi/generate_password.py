import concurrent.futures as futures


# list1 = []
# set1 = set()
#
#
# def add_value(value):
# global list1
# list1.append(value)
# print(round(len(list1) / 99999999 * 100, 1), " %")

#     global set1
#     set1.add(value)
#     print(round(len(set1) / 99999999 * 100, 1), " %")
#
#
# def summator(start, stop):
#     set1 = set()
#     for i in range(int(start), int(stop)):
#         i = str(i)
#         while len(i) < 8:
#             i = "0" + i
#         # add_value(i)
#         set1.add(value)
#     return set1
# print(round(len(set1) / 99999999 * 100, 1), " %")
# with open(f'{start}.txt', 'w') as file:
#     file.writelines(set1)


# with futures.ThreadPoolExecutor(9) as executor:
#     for key, value in {"00000000": "11111111", "11111111": "22222222",
#                        "22222222": "33333333", "33333333": "44444444",
#                        "44444444": "55555555", "55555555": "66666666",
#                        "66666666": "77777777", "77777777": "88888888",
#                        "88888888": "99999999"}.items():
#         # summator(key, value)
#         executor.submit(summator, key, value)

# with futures.ProcessPoolExecutor(9) as executor:
#     for key, value in {"00000000": "11111111", "11111111": "22222222",
#                        "22222222": "33333333", "33333333": "44444444",
#                        "44444444": "55555555", "55555555": "66666666",
#                        "66666666": "77777777", "77777777": "88888888",
#                        "88888888": "99999999"}.items():
#         # summator(key, value)
#         executor.submit(summator, key, value)


# with open('passwords_integers.txt', 'w') as file:
#     for i in range(0, 99999999):
#         i = f"{i}\n"
#         while len(i) < 8:
#             i = "0" + i
#         file.write(i)
#         print(round(int(i) / 99999999 * 100, 1), " %")

def summator(start, stop):
    with open(f'{start}.txt', 'w') as file:
        for i in range(int(start), int(stop)):
            i = str(i)
            while len(i) < 8:
                i = "0" + i
            file.write(f"{i}\n")
    return None


def main():
    dict1 = {"00000000": "11111111", "11111111": "22222222",
             "22222222": "33333333", "33333333": "44444444",
             "44444444": "55555555", "55555555": "66666666",
             "66666666": "77777777", "77777777": "88888888",
             "88888888": "99999999"}
    with futures.ProcessPoolExecutor(len(dict1.items())) as executor:
        for key, value in dict1.items():
            executor.submit(summator, key, value)


def joines():
    list1 = ["00000000", "11111111",
             "22222222", "33333333",
             "44444444", "55555555",
             "66666666", "77777777",
             "88888888"]
    with open(f'number.txt', 'wb') as file:
        for name in list1:
            with open(f'{name}.txt', 'rb') as file1:
                file.writelines(file1.readlines())


if __name__ == '__main__':
    # main()
    joines()
