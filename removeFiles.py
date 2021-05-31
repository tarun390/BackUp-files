import os
import shutil

source = input("Enter folder name (source): ")
destination = input("Enter folder name (destination): ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)

for file in list_of_files:
    shutil.copy((source + file), destination)