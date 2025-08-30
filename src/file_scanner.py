from pathlib import Path


def list_files(source_dir: Path) -> list[Path]:
    files = []
    source_dir.iterdir()
    for file in source_dir.iterdir():
        if file.is_dir():
            files += list_files(file)
        elif file.suffix == ".csv":
            files.append(file)
    return files
