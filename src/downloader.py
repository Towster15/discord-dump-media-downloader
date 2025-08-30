import os
import requests
import more_itertools
from multiprocessing.pool import ThreadPool


def download_link_list(url_list: list[str]) -> None:
    split_url_list = more_itertools.divide(2, url_list)
    ThreadPool(2).map(download_thread, split_url_list)


def download_thread(url_list: list[str]) -> None:
    for url in url_list:
        download_media(url)


def download_media(url: str) -> None:
    response = requests.get(url)
    print(f"ok: {response.ok}, code: {response.status_code}")

    file_ext = url.split(sep="?")[0].split(".")[-1]

    with open(
        get_usable_file_name(str(os.getpid()), file_ext), mode="wb"
    ) as file:
        file.write(response.content)


def get_usable_file_name(file_name: str, file_ext: str) -> str:
    combined_name = f"{os.getcwd()}/output/{file_name}.{file_ext}"
    if os.path.isfile(combined_name):
        i = 1
        combined_name = f"{os.getcwd()}/output/{file_name} ({i}).{file_ext}"
        while os.path.isfile(combined_name):
            i += 1
            combined_name = file_name + f" ({i})." + file_ext

    return combined_name
