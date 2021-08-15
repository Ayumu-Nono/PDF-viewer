def read_file(path: str) -> str:
    with open(path, "r") as f:
        f_str = f.read()
        f_str = f_str.replace("\n", " ")
    return f_str
            


if __name__ == "__main__":
    path = "src/sample/sample.txt"
    read_file(path=path)
    