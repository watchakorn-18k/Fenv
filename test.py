import os
import configparser


config = configparser.ConfigParser()


config.read("example.cfg")


data_string = config.get("data_items")


data_list = data_string.split(",")

print(data_list)


print(len(os.listdir("env_danai#9\Lib\site-packages")))


# with open("r.txt", "w") as f:
#     f.write("")

# for i, v in enumerate(os.listdir("test\env_samai_76\lib\site-packages")):
#     with open("r.txt", "a") as f:
#         if i != 0:
#             f.write("\n" + v)
#         else:
#             f.write(v)
