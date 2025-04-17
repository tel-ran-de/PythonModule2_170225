# "Фильтрация списка строк"
#
#  Дан список строк.
#  Необходимо отфильтровать этот список, оставив только те строки,
#  которые содержат определенную подстроку(keyword), игнорируя регистр.

messages = ["Hello world!", "Important INFO", "debug message", "User Information", "USER logged in"]
keyword = "info"

<<<<<<< HEAD
"Important INFO".lower().find(keyword.lower()) == -1
=======
"Important INFO".lower().find(keyword) == -1
>>>>>>> 313dbff6d8a5cacc923f6a78edd0509c9d16bad3
