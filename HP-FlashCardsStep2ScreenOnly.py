'''
Description: This program simulates math flash cards by generating two random
numbers between a range and a random math operator the number of times a user
indicates. This program also contains other features such as a stopwatch, a
question log and an active score tracker.
'''

# Import libraries
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
import random

# Create main window
window = Tk()
window.title('Flash Cards')
window.geometry('1024x768')

# Create tabs
tab_control = ttk.Notebook(window)

# Create instructions tab
tab_instructions = Frame(tab_control)
tab_control.add(tab_instructions, text = 'Instructions📄')

# Create flash cards tab
tab_flash_cards = Frame(tab_control)
tab_control.add(tab_flash_cards, text = 'Flash Cards')

# Create a tab containing all the previous questions and responses
tab_log = Frame(tab_control)
tab_control.add(tab_log, text = 'Question Log')

tab_control.pack(expand = 1, fill = 'both')

# Content for instructions tab

# Create an empty label
lbl_empty1 = Label(tab_instructions, text='', padx = 105)
lbl_empty1.grid(row = 0, column = 0, columnspan = 3)

# Create a heading label
lbl_heading_instructions = Label(tab_instructions, text = '''Welcome to Hetav's
Flash Cards''', pady = 10, font = ('Arinoe', 15))
lbl_heading_instructions.grid(row = 0, column = 3)

# Create a memorable message
mem_message = 'Where you make your memory stronger'
lbl_memorable = Label(tab_instructions, text = mem_message, font = \
                      ('Arinoe', 15))
lbl_memorable.grid(row = 1, column = 3)

# Create an empty label
lbl_empty2 = Label(tab_instructions, text='', pady = 20)
lbl_empty2.grid(row = 2, column = 3, columnspan = 3)

# Create a label containing instructions to the game
instructions = ''' Flash cards are here to build up your arithmetic skills. In
this game you will be given random numbers between a range that you have
selected and a random math operator and then you will have to answer the
question. You will have the option to select your level, include negative
numbers and an area to indicate how many questions you want to be challenged
with.
 
 
GOOD LUCK and happy solving!
'''
lbl_instructions = Label(tab_instructions, text = instructions, font = \
                         ('Arinoe', 15))
lbl_instructions.grid(row = 3, column = 3,)

# Content for flash_cards tab

# Create variables for question
num1 = 0
num2 = 0
operator = '+'

# Create a variable that contains padding of some labels
padx_row1 = 81
pady_row1 = 20

# Create progress bar
bar = Progressbar(tab_flash_cards, length = 200, style = \
                  'black.Horizontal.TProgressbar')
bar['value'] = 10
bar.grid(row = 0, column = 0, rowspan = 2, columnspan = 12, sticky = W + E)

# Create labels for numbers
lbl_n1 = Label(tab_flash_cards, text = num1, padx = padx_row1, \
               pady = pady_row1, font = ('Arinoe', 45))
lbl_n1.grid(row = 2, column = 0)

lbl_n2 = Label(tab_flash_cards, text = num2, padx = padx_row1, \
               pady = pady_row1, font = ('Arinoe', 45))
lbl_n2.grid(row = 2, column = 2)

# Create operator label
lbl_operator = Label(tab_flash_cards, text = operator, padx = padx_row1, \
                     pady = pady_row1, font = ('Arinoe', 45))
lbl_operator.grid(row = 2, column = 1)

# Create equal sign label
lbl_equal = Label(tab_flash_cards, text = '=', padx = padx_row1, \
                  pady = pady_row1, font = ('Arinoe', 45))
lbl_equal.grid(row = 2, column = 3)

# Create input label 
ans = Entry(tab_flash_cards, width = 6, font = ('Arinoe', 45))
ans.grid(row = 2, column = 4, pady = pady_row1)

# Create empty label for spacing
lbl_empty1 = Label(tab_flash_cards, padx = 10)
lbl_empty1.grid(row = 2, column = 5)

# Create check answer button
check_ans_btn = Button(tab_flash_cards, text = 'Go!', width = 10, \
                       font = ('Arinoe', 15))
check_ans_btn.grid(row = 2, column = 6, columnspan = 5)

# Create an option to indicate number of questions to ask
lbl_num_of_questions = Label(tab_flash_cards, text = 'How many questions:', \
                             font = ('Arinoe', 15))
lbl_num_of_questions.grid(row = 3, column = 0, columnspan = 2)

num_of_questions = Entry(tab_flash_cards, width = 5, font = ('Arinoe', 20))
num_of_questions.grid(row = 4, column = 0, columnspan = 2)

# Create empty label for spacing
lbl_empty2 = Label(tab_flash_cards)
lbl_empty2.grid(row = 5, column = 0)

# Create radio button widgets
selected = IntVar()

lbl_neg_num = Label(tab_flash_cards, text = 'Include negative numbers?', \
                    font = ('Arinoe', 15), pady = 14)
lbl_neg_num.grid(row = 6, column = 0, columnspan = 2)

rad_yes = Radiobutton(tab_flash_cards, text = 'Yes', value = True, \
                      variable = selected, font = ('Arinoe', 15))
rad_yes.grid(row = 7, column = 0)

rad_no = Radiobutton(tab_flash_cards, text = 'No', value = False, \
                     variable = selected, font = ('Arinoe', 15))
rad_no.grid(row = 7, column = 1)

# Create a label that shows whether answer is correct or incorrect
correct_incorrect = 'CORRECT! OR INCORRECT!'

lbl_caption = Label(tab_flash_cards, text = correct_incorrect, \
                    font = ('Arinoe', 15))
lbl_caption.grid(row = 4, column = 3)

# Display image correspondingly
img = 'correctanswer.png'

img_correct = PhotoImage(file = img)
lbl_img = Label(tab_flash_cards, image = img_correct)
lbl_img.grid(row = 4, column = 4)

# superb
# Create empty label for spacing
lbl_empty3 = Label(tab_flash_cards)
lbl_empty3.grid(row = 8, column = 0)

# Create level selector
lbl_level = Label(tab_flash_cards, text = 'Select Level', pady = 10, \
                  font = ('Arinoe', 15))
lbl_level.grid(row = 9, column = 0)

spin_level = Spinbox(tab_flash_cards, from_ = 1, to = 4, width = 5, \
                     font = ('Arinoe', 20))
spin_level.grid(row = 10, column = 0)

# Create reset button
reset_btn = Button(tab_flash_cards, text='Start/Reset', width = 11, \
                   font = ('Arinoe', 14))
reset_btn.grid(row = 10, column = 1)

# Create score label
lbl_score = Label(tab_flash_cards, text = 'Score', font = ('Arinoe', 18))
lbl_score.grid(row = 8, column = 4, columnspan = 5)

# Create label that says incorrect
lbl_incorrect = Label(tab_flash_cards, text = 'Wrong:', font = ('Arinoe', 18))
lbl_incorrect.grid(row = 9, column = 4)

# Create label that says correct
lbl_correct = Label(tab_flash_cards, text = 'Correct:', font = ('Arinoe', 18))
lbl_correct.grid(row = 10, column = 4)


# Create label that says total questions answered
lbl_total = Label(tab_flash_cards, text = 'Total Attempts:', \
                  font = ('Arinoe', 18))
lbl_total.grid(row = 11, column = 4)

# Create score keeping variables
incorrect = 0
correct = 0
total = 0

# Create label that shows total questions incorrect
lbl_incorrect_num = Label(tab_flash_cards, text = incorrect, \
                          font = ('Arinoe', 18))
lbl_incorrect_num.grid(row = 9, column = 5)

# Create label that shows total questions correct
lbl_correct_num = Label(tab_flash_cards, text = correct, font = ('Arinoe', 18))
lbl_correct_num.grid(row = 10, column = 5)

# Create label that shows total questions answered
lbl_total_num = Label(tab_flash_cards, text = total, font = ('Arinoe', 18))
lbl_total_num.grid(row = 11, column = 5)

# Contents of second tab

# Create labels for headers
lbl_heading = Label(tab_log, text = 'The previous questions and answers are:', \
                    pady = 20, font = ('Arinoe', 18))
lbl_heading.grid(row = 0, column = 0, columnspan = 3)

lbl_question = Label(tab_log, text = 'Question', font = ('Arinoe', 15))
lbl_question.grid(row = 1, column = 0)

lbl_user_ans = Label(tab_log, text = 'Your answer', font = ('Arinoe', 15))
lbl_user_ans.grid(row = 1, column = 1)

lbl_correct_ans = Label(tab_log, text = 'Correct answer', font = ('Arinoe', 15))
lbl_correct_ans.grid(row = 1, column = 2)

# Display symbol showing whether correct using a label
#use insert to add a checkbox

# Create a ScrolledText Widget
previous_questions = scrolledtext.ScrolledText(tab_log, width = 67, height = 30)
previous_questions.grid(row = 2, column = 0, columnspan = 3)

# Keep window open
window.mainloop()