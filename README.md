# wordleSolver
### helps solve wordle riddles. 
### Disclaimer: Just an afternoon fun project, because I was frustrated with worldle and couldn't find a solution to a specific riddle.

## How to use
If you start from scratch you can just run `python wordle.py` and then go through the questions.
It will run the default with 5 letters for the word.
To see the options do `python wordle.py --help`.

### Basically:
- -n or --length: To choose a word with arbitrary length.
- --base: If you want to start with a specific word.
- --mask: The mask on the current word, necessary if --base is selected.
- --blacked: Not necessary but helpful if program is used from any row other then 1 onwards. For example `--blacked erqpdhr` means non of these letters can be part of the word. 

## IDEAS:
- formalize desired parameters and cache cleansed version based on that.
- define function to get rid of words that are not in wordle dictionary (and save in a "know these exist" sort of database).
- weigh words in importance based on how common they are.