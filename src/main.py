from datetime import datetime
import os
from pathlib import Path
import tkinter.filedialog
from multiprocessing import Pool

import more_itertools

from file_scanner import list_files
from link_collector import collect_links
from downloader import download_link_list
from slow_dl import slow_download

# 1. check output folder exists
# 2. list all files
# 3. collect links from all files
# 4. start all attachments downloading
# 5. save all contents list to file

if __name__ == "__main__":
    out_path = os.getcwd() + "/output"

    # 1. check output folder exists
    if Path(out_path).exists() and Path(out_path):
        print("exists!")
    else:
        os.mkdir(out_path)

    old_date = datetime(1970, 1, 1)
    new_date = datetime.now()

    attachment_links = []
    content_links = []

    # 2. list all files
    # 3. collect links from all files
    for file in list_files(
        Path(tkinter.filedialog.askdirectory(mustexist=True))
    ):
        att_links, cont_links = collect_links(
            str(file.absolute()), False, False, old_date, new_date
        )
        attachment_links += att_links
        content_links += cont_links

    with open(
        os.getcwd() + "/output/att.txt", "w", encoding="utf8", newline=""
    ) as file:
        for link in attachment_links:
            file.write(f"{link}\n")

    # # 5. save all contents list to file
    with open(
        os.getcwd() + "/output/cont.txt", "w", encoding="utf8", newline=""
    ) as file:
        for link in content_links:
            file.write(f"{link}\n\n")

    slow_download(attachment_links)

    # downloading all images
    # attachment_link_chunks = more_itertools.divide(
    #     os.cpu_count(), attachment_links
    # )
    # with Pool(os.cpu_count()) as p:
    #     for item in p.imap_unordered(
    #         download_link_list, attachment_link_chunks
    #     ):
    #         print(item)
