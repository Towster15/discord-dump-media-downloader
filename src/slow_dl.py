import requests
import os

# import time
import logging


logging.basicConfig(
    filename="logfile.log", filemode="a", encoding="utf-8", level=logging.INFO
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


def slow_download(url_list) -> None:
    for i in range(0, len(url_list)):
        if i % 100 == 0:
            print(f"at item {i} or {len(url_list)}")
        url = url_list[i]
        response = requests.get(url, headers=headers)
        # print(f"ok: {response.ok}, code: {response.status_code}")

        if response.ok:
            file_ext = url.split(sep="?")[0].split(".")[-1]
            if len(file_ext) > 5:
                logging.warning(f"failed to get file ext for {i}")
            else:
                with open(
                    f"{os.getcwd()}/output/{i}.{file_ext}", mode="wb"
                ) as file:
                    file.write(response.content)
            # time.sleep(0.1)
        elif response.status_code == 404:
            logging.info(f"404 for item {i}")
        else:
            logging.critical(
                f"got code {response.status_code}, quitting at {i}"
            )
            break
