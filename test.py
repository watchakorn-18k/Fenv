import os
import glob

# os.chdir("test")
# print(os.getcwd())
# versions =
# print(versions)
# if versions:
#     latest_version = max(versions)
#     os.chdir(latest_version)
# else:
#     print("No Python installations found in env_danai#20/lib/")
os.chdir("test")

path_lib_python = "".join(glob.glob("env_danai#20/lib/python*"))
os.chdir(f"{path_lib_python}/site-packages")
print(os.getcwd())
