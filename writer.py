def write_file(path: str, contents: str) -> None:
    with open(path, "w") as f:
        f.write(contents)
