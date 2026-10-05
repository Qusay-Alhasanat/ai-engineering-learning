from text_analyzer.analyzer import analyze_text, validate_text


def main() -> None:
    text = input("Enter text: ")

    if not validate_text(text):
        print("Text cannot be empty.")
        return

    result = analyze_text(text)

    print(result)
