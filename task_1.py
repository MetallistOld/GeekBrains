import re


def email_parse(email):
    parsed = re.findall(r"([^@&]+)@([\w-][\w\.-]*\.[\w-]{2,})$", email) # Сложно было регулярку сделать

    if not parsed:
        raise ValueError(f"wrong email: {email}")
    return dict(zip(["username", "domain"], parsed[0]))


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
