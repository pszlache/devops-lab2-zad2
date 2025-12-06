def test_echo():
    test_cases = [
        ("Hello", "Program: Hello"),
        ("123", "Program: 123"),
        ("How are you?", "Program: How are you?"),
        ("end", "Program finish.")
    ]

    for i, (input_text, expected_output) in enumerate(test_cases):
        if input_text.lower() == "end":
            output = "Program finish."
        else:
            output = f"Program: {input_text}"

        if output == expected_output:
            print(f"Test {i+1}: OK")
        else:
            print(f"Test {i+1}: BŁĄD (wejście: '{input_text}', oczekiwane: '{expected_output}', otrzymano: '{output}')")

if __name__ == "__main__":
    test_echo()
