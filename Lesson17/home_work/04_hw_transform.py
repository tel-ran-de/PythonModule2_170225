

# У вас есть список строк, некоторые из которых содержат email-адреса.
# Вам нужно извлечь все email-адреса и привести их к нижнему регистру.
# email-адреса содержат символ '@'.

log_entries = [
    "User logged in: john.doe@example.com",
    "Error occurred",
    "New user registered: Jane_Smith@Example.ORG",
    "Another log",
    "Contact us at support@test.co.uk"
]

email_show = list(filter(lambda log_entry: '@' in log_entry, log_entries))
astring = email_show

email_lower = list(map(lambda email: email.lower(), email_show))
print(email_lower)
