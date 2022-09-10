# Text-Based-Adventure-Game
For Year 11 Computer Science General
Requirements
  The requirements to the task is to make a text based adventure game with comments, if statements, loops, three or more rooms, and adding my own twist and features to it.
How to Play
  You can play the game by typing in the suggested actions to interact with the environment, or you can type quit to quit the game.
Features
  My game has a choreographed dance fight in it, a light switch, an easter egg when you die.
  I have an easter egg in the game, it activates when you die and restart. When you go into the vent towards the end, it will call you a ‘sussy baka’.
  The way the dance (boss) fight works is that it picks a random number between 1 – 10. If the number is greater than 4, the enemy will lose health. Each number from 5 – 10 has a different dance move. If the number is less than 4, the player will lose heath. Every number from 1 – 4 has a different dance move.
Expected Input and Output Values
  The expected input values would be ‘pickup’, ‘inspect switch’, ‘forward’, ‘backward’, ‘look’
  You type forward, it describes the next room.
  You type inspect switch, describes the events that follow to turning on the switch
  You type backwards, it describes the previous room
  You type look, it describes the room you’re in.
Input Values Used to Test
  To test the fight sequence, I made a new python file and copied just the useful stuff like the dictionary with ‘ehealth’ and ‘phealth’ and the while loop for the staying in the boss fight until the fight is over.
Issues Encountered
  I encountered an issue where I made the variable for the boss fight ‘random’ and the random variable didn’t work. The reason it didn’t work is because ‘random’ is a keyword already used in the program. The way I found out was I asked Mrs. Chomiak and she told me about that.
  I didn’t know how to end the game at the end since I already had an exit function which said something like ‘goodbye, thanks for playing’. The way I made the end game part was by using ‘sys.exit()’ from importing sys. I thought it looked a bit scrappy as it looks like the game crashes, so I made a little story to make it seem like it was on purpose.
  I tried to carry a variable across different functions, so I figured out I needed to make a state in the dictionary for the ‘playername’ which I assigned to a variable in one function. I could then use the ‘playername’ later on in the game. Then to make the name uppercase for one part, I had to use the ‘.upper’ function with the state.
  To test rooms working, I used print statements with random text to make sure I could make it to a room.
