import csv
from datetime import datetime

# ID,Timestamp,Contents,Attachments
# timestamp: 2021-03-15 17:59:31.341000+00:00

ID = 0
timestamp = 1
contents = 2
attachments = 3


def collect_links(
    file_path: str,
    sort_by_old: bool = False,
    sort_by_new: bool = False,
    oldest_date: datetime = datetime(1970, 1, 1),
    newest_date: datetime = datetime.now,
) -> tuple[list, list]:
    attachment_links = []
    content_links = []

    with open(file_path, encoding="utf8", newline="") as csvfile:
        data = list(csv.reader(csvfile))
    data.pop(0)

    for row in data:
        msg_date = datetime.fromisoformat(row[timestamp])
        if row[attachments] != "" and check_date(
            msg_date, sort_by_old, sort_by_new, oldest_date, newest_date
        ):
            attachment_links.append(row[attachments])
        if "http" in row[contents] and check_date(
            msg_date, sort_by_old, sort_by_new, oldest_date, newest_date
        ):
            # TODO: split URL out from the rest of the message
            #  string.split() and then search for http/https://
            # content_links.append(row[contents])
            msg = row[contents].split(" ")
            for part in msg:
                if "http://" in part or "https://" in part:
                    content_links.append(part)

    # print(attachment_links, content_links)
    return attachment_links, content_links


def check_date(
    msg_date: datetime,
    sort_by_old: bool,
    sort_by_new: bool,
    oldest_date: datetime,
    newest_date: datetime,
) -> bool:
    if not (sort_by_old and sort_by_new):
        return True
    elif sort_by_old and sort_by_new and oldest_date < msg_date < newest_date:
        return True
    elif sort_by_old and msg_date > oldest_date:
        return True
    elif sort_by_new and msg_date < newest_date:
        return True
    else:
        return False
