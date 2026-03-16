# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The hints told you to the opposite direction of which you needed to go. I expected the hints to be correct. 
- When you changed the dificulty to hard the game got easier. I expected the hard difficulty to give the user a greater window of numbers to choose from. 
- You arent able to start a new game if you have already won. I expect it to start a new game regardless if you have already won. 
- The pannel shows your allowed 8 attempts but the game started with 7 attempts left. I expected it to say you have 8 attempts left at the beginning of the game.

---

## 2. How did you use AI as a teammate?

- I used Claude by telling it which file and line number to fix for the two bugs I found. 
- When I moved the check_guess function to the logic_utils.py file I had it explain why the function became smaller once it was moved.  
- I was able to verify the changes in the game by checking after each bug I fixed by playing the game. 
---

## 3. Debugging and testing your fixes

- I verified my repairs after each fix. For example when I fixed the hint bug I played the game and guessed higher lower and ther secret number to verify it worked before moving on to the next bug. 
- When I first ran pytest it gave me an error because the test file could not find logic_utils. This showed me how python imports work.
- I used AI to help generate the test because I have not used pytest before. I also had it explain the sytax for pytest so that I know what it is doing. 

---

## 4. What did you learn about Streamlit and state?

- I noticed when testing my bug fixes I did not have to rerun the application in the terminal each time and was able to just refresh the page. State is how streamlit remembers between reruns. Without it every time you submitted an answer it would start over. 

---

## 5. Looking ahead: your developer habits

- In the future I will start referencing file names and even line numbers when prompting. 
- Also, moving forward I want to look so to see if I can find the problem/solution first before just prompting AI to fix it. 
- By doing this project I believe that it is important to understand the code your working on and the code the AI generates. 




