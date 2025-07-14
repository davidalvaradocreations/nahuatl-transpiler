REPLACEMENTS = {
    "tlahcuiloa": "print",
    "tlatequitl": "def",
    "moma": "return",
    "queniuh": "if",
    "ixquich": "else",
    "cuix": "while",
    "ipan": "for",
    "queme": "True",
    "ahmo": "False",
    "huan": "and",
    "o": "or",
    "tlatlaniz": "input",
    "lista": "list",
}

def transpile(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()
    for nahuatl, python in REPLACEMENTS.items():
        code = code.replace(nahuatl, python)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Transpiled {input_file} to {output_file}")

if __name__ == "__main__":
    # Change these filenames as needed
    transpile("math_example.nah", "output.py")
