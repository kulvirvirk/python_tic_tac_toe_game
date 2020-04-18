 # 1. create a dictionary to store the three rows(or 9 possible values) for the game these strings should be empty in the begining
 # 2. print out the board with default values from the board_values dictionary 

board_values = {
  'top-L': ' ', 'top-M':'X', 'top-R':' ',
  'mid-L': 'X', 'mid-M':'X', 'mid-R':' ',
  'low-L': 'O', 'low-M':'O', 'low-R':'O', }

 # 2. print out the board with default values from the board_values dictionary 
print(board_values['top-L'] + '|' + board_values['top-M'] + '|' + board_values['top-R'] + '\n'\
 + '-----' + '\n'\
 + board_values['mid-L'] + '|' + board_values['mid-M'] + '|' + board_values['mid-R']  + '\n'\
 + '-----' + '\n'\
 + board_values['low-L'] + '|' + board_values['low-M'] + '|' + board_values['low-R'] 
  )
