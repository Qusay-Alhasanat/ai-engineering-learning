import string


def clean_text(text: str) -> str:
    text = text.lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    text = " ".join(text.split())

    return text
