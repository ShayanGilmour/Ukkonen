# Ukkonen's Algorithm
Ukkonen's Algorithm implemented by python with tkinter interface

There are 4 code, the general principle of all of them are the same; All of them create a (generalized) suffix tree in linear time. But each of them uses this tree to solve different problems.

## Phase 1
Inputs several strings. Then a pattern, and searchs for the pattern in the strings. (Linear Time)

#### Input:
First, the target strings: For every string, at a line there should be the single character `>`, then at the **next** line, the corresponding string. It's also possible to browse the input file. After that, you should press the `Create Suffix Tree` button. After that, you can enter the searching pattern.

#### Process:
It creates a generalized suffix tree of the target strings, and searches the pattern in the tree.

#### Output:
The starting indices of the strings where the pattern was found.

## Phase 2
Finding the longest repeating substring.

#### Input:
First, you should enter the main string. Then after pressing the `Create Suffix Tree` button, you can enter the least number of repetition required.

#### Output:
It outputs the longest substring of the string which repeats in the string as required.

## Phase 3
Finding the longest common substring among some strings.

#### Input:
First, the target strings: For every string, at a line there should be the single character `>`, then at the **next** line, the corresponding string. After that, you should press the `Create Suffix Tree` button.

Next, enter the number `k`': number of the main strings that must have a substring in common.

#### Output:
It finds the longest string that at least `k` strings of the main strings contain that string.

## Phase 4
Finding the longest palindrome substring in the main string.

#### Input:
Enter the main string.

#### Output:
It finds the longest palinedrome substring of the main string.

### Samples:

<p float="left">
  <img src="https://user-images.githubusercontent.com/12760574/130654338-f8206a68-012c-4120-af32-0b63549129fc.png" width="300" />
  <img src="https://user-images.githubusercontent.com/12760574/130654344-ee6d11be-37db-4fb5-a664-5be4a989c6c8.png" width="300" /> 
  <img src="https://user-images.githubusercontent.com/12760574/130654348-bda5b2f2-fa98-4acc-9504-ee1250b50b50.png" width="300" /> 
  <img src="https://user-images.githubusercontent.com/12760574/130654355-1e149d53-c7e1-4ef6-a10d-4f585c337153.png" width="300" />
</p>


