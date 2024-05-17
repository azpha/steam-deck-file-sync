import requests
import os
from time import sleep

folder_to_monitor = "/home/deck/Videos"
target_url = "http://local_ip:9999/upload"

if __name__ == "__main__":
    last_known_list = os.listdir(folder_to_monitor)
    while True:
        new_known_list = os.listdir(folder_to_monitor)

        if len(new_known_list) > len(last_known_list):
            print("change detected!")
            for element in new_known_list:
                if element not in last_known_list:
                    file_path = os.path.join(folder_to_monitor, element)
                    read_file = open(file_path, "rb")
                    response = requests.post(target_url, files = { "file": read_file })

                    if response.ok:
                        print("file uploaded!")
                    else:
                        print("something went wrong uploading that file!")

        last_known_list = new_known_list
        sleep(5)
                    