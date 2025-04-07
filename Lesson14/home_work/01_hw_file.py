def log(text, file="log.txt"):
    with open(file, "a", encoding="utf-8") as f:
        f.write(text + "\n")


log("hello world")  # Записывает "hello world"
log("message", "log01.txt")  # Записывает "message" в log01.txt
