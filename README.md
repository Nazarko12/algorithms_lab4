* Description of the laboratory:

Two participants play a linguistic game. At the beginning of the game there is a list of N words.
The first player chooses an arbitrary word w1 and deletes one arbitrary letter from it
so to get another word w2 from this list. After that the course passes to
another player, and he tries to do the same with the word w2.
The game ends in one of two cases:
• There is one word left.
• It is impossible to delete any letter so as to get another word from the dictionary.

Determine the length of the maximum chain that can be achieved in this game
given words.

* Problem solving:

In line 8 of his laboratory, a dictionary has been created, which is currently empty. 
The variable "maximum chain of letters" was also created, which was assigned zero at the beginning.

Used the loop "for" to search for an available word in the dictionary of words. 
Variable iterator_of_start = 0, because we start the game with the first word in the line.
Variable current_max_word = 1, because we started the selection with a random word.

In the "while" cycle:

As long as the variable iterator_of_start <len (available_word) :,
all possible subsequent words formed from the length of the existing word will be written.
By going through all the possible options, you can achieve the maximum length of this chain of words.

Line 25 has a function that is designed to read words from a file.
This_date = [] is an array of specified letters. The loop assumes the moment when the word is equal to an empty line. 
Then we leave the cycle and add this word to the end of the list.

 Print(largest_string_chain(words)).
 
 *Using:
 
 Programming language: Python.
 
 Firstly, download repository: git clone https://github.com/Nazarko12/lab4.git.
 Then you need to open package: "cd lab4".
 Go to the branch "algorithms_lab4": "git checkout algorithms_lab4".
 Run the file: words_chain.py.
 
 
 
