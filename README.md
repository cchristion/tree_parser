# tree_parser

This Python script converts the output of the `tree` command into a list of relative file paths.

## Instructions

- **Run the Python script:**
   ```sh
   python tree_parser.py input.txt
   ```
- **Alternatively, save the output to a file:**
   ```sh
   python tree_parser.py input.txt > output.txt
   ```
- **Demo**
   ```sh
   # cd into tree_parser directory
   rm -r test 1.txt 2.txt
   mkdir -p test/{a,b,c}/{d,e,f}
   touch test/{a,b,c}/{d,e,f}/{1,2,3}.txt
   touch test/{1,2,3}.txt
   tree test > input.txt
   python tree_parser.py input.txt
   ```
