# Nahuatl-Python Transpiler

## Description

This is a simple translator that allows Nahuatl speakers to write and learn coding in their native language.
The project bridges the gap between technology and indigenous language speakers by enabling programming with Nahuatl-inspired keywords.
Feedback from Native speakers is especially welcome to improve vocabulary accuracy and adapt for different dialects.

## Features

- Define functions with tlatequitl (Nahuatl for "def")
- Print output using tlahcuiloa ("print")
- Basic control flow: queniuh (if), ixquich (else), cuix (while), ipan (for)
- Boolean values: queme (True), ahmo (False)
- Logical operators: huan (and), o (or)
- User input via tlatlaniz (input)
- List support with lista (list)

## How to Use

1. Write your Nahuatl code in a file with the `.nah` extension (e.g., example.nah).

2. Open the nahuatl_transpiler.py file in a text editor.

3. Find the line near the bottom:

    transpile("example.nah", "output.py")

4. Change "example.nah" to your Nahuatl code filename, and "output.py" to your desired output Python filename.

5. Save the file.

6. Run nahuatl_transpiler.py in your Python environment (IDLE, command prompt, etc.).

7. Run the generated Python file (output.py) to see your program’s output.

## Examples

Example Nahuatl code (example.nah):

tlatequitl saludo():  
    tlahcuiloa("Niltze, macehualmeh!")  
    moma queme

saludo()

Translates to Python (output.py):

def saludo():  
    print("Niltze, macehualmeh!")  
    return True

saludo()

## Community & Sharing

This project is designed not only to help individuals learn coding in Nahuatl but also to encourage users to teach and share this knowledge with others in their community.  
Spreading programming skills through the Nahuatl language can empower more people and help preserve cultural heritage through technology.

## Contributing

Contributions are welcome!  
If you find bugs, have feature ideas, or want to improve the Nahuatl vocabulary, please open an issue or submit a pull request.  
Native speakers’ feedback is especially appreciated.

## License

This project is open source and available under the MIT License.

## Contact

Created by David Alvarado.  
Feel free to reach out via email at davida.create@proton.me or on GitHub.

## Acknowledgments

Thanks to all who inspire indigenous language tech projects and open source communities.
