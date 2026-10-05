import string


def validate_text(text: str) -> bool:
    return bool(text.strip())


def clean_text(text: str) -> str:
    text = text.strip().lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, " ")

    return text


def split_words(text: str) -> list[str]:
    return text.split()


def count_characters(text: str) -> int:
    return len(text)


def count_words(words: list[str]) -> int:
    return len(words)


def count_word_frequency(words: list[str]) -> dict[str, int]:
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def analyze_text(text: str) -> dict[str, object]:
    cleaned_text = clean_text(text)
    words = split_words(cleaned_text)

    return {
        "character_count": count_characters(cleaned_text),
        "word_count": count_words(words),
        "word_frequency": count_word_frequency(words),
    }
