# #Curs 4
# import copy
# players = [
#  {
#     "first_name": "John",
#     "last_name": "Doe",
#     "rank": 3,
# },
#
# {
#     "first_name": "Kevin",
#     "last_name": "McDonald",
#     "rank": 1,
#
# },
#     {
#         "first_name": "Bradd",
#         "last_name": "Kelvin",
#         "rank": 2
#
#     },
#
# ]
# print(players)
# sorted_players = sorted(players, key = lambda player: player["rank"])
# print(sorted_players)
#
#
# def check_top_3_player(player):
#     updated_player = copy.deepcopy(player)
#     updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
#     return updated_player
#
#
# players_with_top_3_value = map(check_top_3_player, players)
# print(list(players_with_top_3_value))
#
# first_list = [x for x in range(1, 10)]
# second_list = [x for x in range(10, 100, 10)]
# third_list = [x for x in range(100, 3000, 100)]
#
# print(first_list)
# print(second_list)
# print(third_list)
#
# for zip_item in zip(first_list, second_list, third_list):
#     first_element, second_element, third_element = zip_item
#     print( first_element, second_element, third_element)
#
#
# first_list = [x for x in range(10)]
# even_squared_number = [x ** 2 for x in first_list if x % 2 == 0 and x > 0]
# print(even_squared_number)


# with open("hello.txt", "w") as file:
    # file.write("Hello world!")

# import csv
#
# with open("data.csv", "r") as csv_file:
#     rows = csv.reader(csv_file, delimiter=",")
#     for rows in rows:
#         print(rows)
#
# new_cars = [
#     ["Dacia", "Logan", 2005, 75],
#     ["Renault", "Clio", 2005, 75]
#
# ]
#
# with open("data.csv", "a") as csv_file:
#     csv_writer = csv_writer(csv_file, delimiter=",")
#
#     for new_cars in new_cars:
#         csv_writer.writerows(new_car)

