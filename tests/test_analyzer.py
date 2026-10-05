from text_analyzer.analyzer import (
    analyze_text,
    clean_text,
    count_characters,
    count_word_frequency,
    count_words,
    split_words,
    validate_text,
)


# validate_text


def test_validate_text_with_valid_text():
    result = validate_text("Hello")

    assert result is True


def test_validate_text_with_empty_text():
    result = validate_text("")

    assert result is False


def test_validate_text_with_whitespace_only():
    result = validate_text("   ")

    assert result is False


# clean_text


def test_clean_text_strips_and_lowercases():
    result = clean_text("  Hello WORLD  ")

    assert result == "hello world"


def test_clean_text_handles_punctuation():
    result = clean_text("Hello, world!")

    assert result == "hello  world "


def test_clean_text_does_not_merge_words():
    result = clean_text("hello,world")

    assert result == "hello world"


# split_words


def test_split_words_splits_text_into_words():
    result = split_words("hello world python")

    assert result == ["hello", "world", "python"]


def test_split_words_handles_multiple_spaces():
    result = split_words("hello   world    python")

    assert result == ["hello", "world", "python"]


# count_characters


def test_count_characters_counts_all_characters():
    result = count_characters("hello world")

    assert result == 11


def test_count_characters_with_empty_text():
    result = count_characters("")

    assert result == 0


# count_words


def test_count_words_counts_words():
    result = count_words(["hello", "world", "python"])

    assert result == 3


def test_count_words_with_empty_list():
    result = count_words([])

    assert result == 0


# count_word_frequency


def test_count_word_frequency_counts_unique_words():
    result = count_word_frequency(["hello", "world", "python"])

    assert result == {
        "hello": 1,
        "world": 1,
        "python": 1,
    }


def test_count_word_frequency_counts_repeated_words():
    result = count_word_frequency(["python", "is", "python"])

    assert result == {
        "python": 2,
        "is": 1,
    }


def test_count_word_frequency_with_empty_list():
    result = count_word_frequency([])

    assert result == {}


# analyze_text


def test_analyze_text_returns_correct_results():
    result = analyze_text("Hello, hello! WORLD")

    assert result == {
        "character_count": 19,
        "word_count": 3,
        "word_frequency": {
            "hello": 2,
            "world": 1,
        },
    }