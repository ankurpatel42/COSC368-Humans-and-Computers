from tkinter import *
from tkinter.ttk import *
import time
import random
import csv

#configuration of the keyboard
configuration = "static"
#configuration = "dynamic"

letters_seen = {}
               
start = time.time()

#number of times going through block
n = 2
num_letters = 6
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
block = []
n_blocks = []

#num_letters from the alphabet added to the block of length n 
while len(block) != num_letters:
    letter_to_add_to_block = letters[random.randrange(0, len(letters))]
    letters.pop(letters.index(letter_to_add_to_block))
    block.append(letter_to_add_to_block)
while n > 0:
    random.shuffle(block)
    n_blocks += block
    n -= 1
#initial letter to find
letter_to_find = n_blocks[0]

def character_click_count(letter_to_find, letters_Seen):
    if letter_to_find in letters_seen:
        letters_seen[letter_to_find] += 1
    else:
        letters_seen[letter_to_find] = 1    

def clickButton(character_clicked, letter_to_find):
    
    global start
    global letters_seen
    global board
    global frame 
    global configuration
    
    letter_to_find = labeltext.get()
    
    if character_clicked == letter_to_find:
        total_time = "{:.1f}".format((time.time() - start) * 1000)
        character_click_count(letter_to_find, letters_seen)
        spamwriter.writerow(["Ankur"] + [configuration] + [letter_to_find] + [letters_seen[letter_to_find]] + [total_time])
        n_blocks.pop(n_blocks.index(letter_to_find))      
        if n_blocks == []:          
            labeltext.set("All blocks complete!")
        else:
            letter_to_find = n_blocks[0]
            labeltext.set(letter_to_find)
            if configuration == "dynamic":
                populate_keyboard(create_keyboard(), frame, letter_to_find)             
            start = time.time()
        
    
def populate_keyboard(board, frame, letter_to_find):
    for i in range(len(board)):
        for j in range(len(board[i])):
            buttonframe = Frame(frame, height=32, width=32)
            buttonframe.grid(column=(2 * j)+i, row=i, columnspan=2)
            buttonframe.pack_propagate(0)        
            button = Button(buttonframe, text=board[i][j],command=lambda x=board[i][j]:clickButton(x, letter_to_find))
            button.pack(fill=BOTH, expand=1)    
            

def create_keyboard():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    list_alphabet = list(alphabet)
    random.shuffle(list_alphabet)
    first_row = ''.join(list_alphabet[0:10])
    second_row = ''.join(list_alphabet[10:19])
    third_row = ''.join(list_alphabet[19:])
    board = [first_row, second_row, third_row]
    return board

with open('experiment_{}_log.txt'.format(configuration), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)  

    window = Tk()
    frame = Frame(window, borderwidth=1, relief=RIDGE, height=32, width=32)
    frame.pack(side=BOTTOM, padx=10, pady=10)
    labeltext = StringVar()
    label = Label(window, textvariable=labeltext)
    labeltext.set(letter_to_find)
    label.pack()
    board = create_keyboard()
    populate_keyboard(board, frame, letter_to_find)
    window.mainloop()
    

