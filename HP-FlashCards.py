'''
Description: This program simulates math flash cards by generating two random
numbers between a range and a random math operator the number of times a user
indicates. This program also contains other features such as a stopwatch, a
question log and an active score tracker.
'''

# Bibliography
# From this source I learned to create a stopwatch
# https://youtu.be/mdfuJPGLhPM

# Import libraries
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
from tkinter import messagebox
import random

# Custom functions

# function that changes the text of a widget
# input: name of widget, any value
# returns: nothing
def widget_change(widget, value):
    widget.configure(text = value)
    
# function that changes the numbers in the math question 
# input: integer, integer
# returns: nothing
def random_numbers(minimum, maximum):
    # Call on global variables
    global num1, num2, operator
    
    # Set local variable
    asking = True
    
    # Check if the user wants to include negative numbers
    negative = int(selected_neg_num.get())
    
    while asking:
        # Generate two random numbers
        num1 = random.randint(minimum, maximum)
        num2 = random.randint(minimum, maximum)
        if negative == 1:
            # Decide whether to make number negative and if yes decide which one
            include_neg_or_not = int(random.choice('1234'))
            if include_neg_or_not == 1:
                # Make first number negative
                num1 = num1 * -1
            elif include_neg_or_not == 2:
                # Make second number negative
                num2 = num2 * -1
            elif include_neg_or_not == 3:
                # Make both numbers negative
                num1 = num1 * -1
                num2 = num2 * -1
                # Otherwise do not make any numbers negative
        
        # If the operator is not division then just display the numbers
        if operator == '-' or operator == 'x' or operator == '+':
            asking = False
        else:
            # Check that the second number evenly divides into the first
            if num1 % num2 == 0:
                asking = False
        
    # Change the label that contains the numbers for the question
    widget_change(lbl_n1, num1)
    widget_change(lbl_n2, num2)

# function that changes the math operator
# input: none
# returns: nothing
def change_operator():
       # Call on the global variable
    global operator
    
    # Check if division should be included
    division = int(selected_division.get())
    
    # Pick a random operator
    if division == 1:
        operator = random.choice('+-x÷')
    else:
        operator = random.choice('+-x')
        
    # Change the label containing the operator
    widget_change(lbl_operator, operator) 

# function that validates the number of questions
# input: none
# returns: nothing
def get_num_of_q():
    # Call on global variables
    global valid_num_of_q, num_q_first_selection
    
    # Validate the number of questions and give error if invalid
    num_of_q = num_of_questions.get()
    message = 'The available range is from 1 to 100, inclusive.'
    
    # Validate the number of questions and give error if invalid
    try:
        if int(num_of_q):
            if int(num_of_q) > 0 and int(num_of_q) <= 100:
                valid_num_of_q = True
                num_q_first_selection = float(num_of_q)
            else:
                valid_num_of_q = False
                messagebox.askokcancel('Invalid number of questions', message)
    except:
        valid_num_of_q = False
        messagebox.askokcancel('Invalid number of questions', message)
    
# function that validates the level
# input: none
# returns: nothing
def get_level():
    # Call on global variables
    global valid_level, level
    
    # Get the level
    level = spin_level.get()
    
    # Set error message
    message = 'Please select a level from 1 to 4, inclusive.'
    
    # Check if level data type is valid else give error message
    try:
        if int(level):
            if int(level) > 0 and int(level) <= 4:
                valid_level = True
                level = int(level)
            else:
                valid_level = False
                messagebox.askokcancel('Invalid level', message)
    except:
        valid_level = False
        messagebox.askokcancel('Invalid level', message)

# function that starts the stopwatch
# input: none
# returns: nothing
def start_stopwatch():
    # Call on global variable
    global time_ticking
    
    # Start updating the time if stopwatch is not already on
    if not time_ticking:
        # Add a second by calling the update_stopwatch function
        update_stopwatch()
        
        # Make time_ticking true
        time_ticking = True

# function that resets the the stopwatch
# input: none
# returns: nothing
def reset_stopwatch():
    # Call on global variables
    global time_ticking, hours, minutes, seconds
    
    # Stop stopwatch
    lbl_stopwatch.after_cancel(add_time)
    
    # Make time_ticking false
    time_ticking = False
    
    # Reset variables because time has stopped
    hours, minutes, seconds = 0, 0, 0
    
    # Reset label
    lbl_stopwatch.configure(text = '00:00:00')

# function that resets and starts the stopwatch at the same time
# input: none
# returns: nothing
def reset_start_stopwatch():
    # Call on global variables
    global time_ticking, hours, minutes, seconds
    
    # Reset the stopwatch and start it again
    if not time_ticking:
        
        # Stop stopwatch
        lbl_stopwatch.after_cancel(add_time)
        
        # Make time_ticking false
        time_ticking = False
        
        # Reset variables because time has stopped
        hours, minutes, seconds = 0, 0, 0
        
        # Reset label
        lbl_stopwatch.configure(text = '00:00:00')
        
        # Start adding to the time every second
        update_stopwatch()
        
        # Make time_ticking true
        time_ticking = True

# function that pauses the stopwatch
# input: none
# returns: nothing
def pause_time():
    # Call on global variable
    global time_ticking
    
    # Stop the stopwatch if the stopwatch is on
    if time_ticking:
        # Stop the time
        lbl_stopwatch.after_cancel(add_time)
        
        # Make time_ticking false
        time_ticking = False

# function that updates the time every second
# input: none
# returns: nothing
def update_stopwatch():
    # Note: if window is closed while stopwatch is running then it sometimes
    # gives the following error:
    # invalid command name "1550731888256update_stopwatch"
    # while executing
    # "1550731888256update_stopwatch"
    # ("after" script)

    # Call on global variables
    global hours, minutes, seconds, add_time
    
    # Add seconds
    seconds += 1
    
    # Add to the minutes if its been 60 seconds and reset the seconds
    if seconds == 60:
        minutes += 1
        seconds = 0
        
    # Add to the hours if its been 60 minutes and reset the minutes
    if minutes == 60:
        hours += 1
        minutes = 0
    
    # Change stopwatch on screen
    # F-Strings or format-strings help to add variables in the string, in this
    # particular case it helps to add the leading zeros that make the aesthetic
    # better
    hours_on_screen = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_on_screen = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_on_screen = f'{seconds}' if seconds > 9 else f'0{seconds}'
        
    # Change the stopwatch label to display the increasing time
    lbl_stopwatch.configure(text = hours_on_screen + ':' + minutes_on_screen + \
                            ':' + seconds_on_screen)
    
    # Update the time every second
    add_time = lbl_stopwatch.after(1000, update_stopwatch)

# function that resets the score
# input: none
# returns: nothing
def reset_score():
    # Call global variables 
    global incorrect, correct, total, img, counter2, counter, increment
    
    # Reassign some global variables
    incorrect, correct, total, counter, increment, counter2 = 0, 0, 0, 0, \
                                                                   0, 0
    
    # Call on a function to reset the score
    widget_change(lbl_incorrect_num, incorrect)
    widget_change(lbl_correct_num, correct)
    widget_change(lbl_total_num, total)
    
    # Configure the image and its caption so that they are blank
    img = 'blankimage.png'
    image.configure(file = img)
    lbl_caption.configure(text = '')
    
    # Reset the progress bar
    bar['value'] = 0
    
# function that calls on other functions to reset the score, get the number
# of questions, the level, to reset and start the stopwatch
# input: none
# returns: nothing
def start_reset():
    # Call global variables 
    global valid_num_of_q, valid_level, clicked_start, num1, num2, operator, \
           hours, minutes, seconds, time_ticking
    
    # Check if start/reset button was clicked earlier
    if clicked_start:
        # Focus the cursor on the entry box asking for number of questions
        num_of_questions.focus()

        # Reset the numbers and operator
        num1, num2, operator = 0, 0, '?'
        widget_change(lbl_n1, num1)
        widget_change(lbl_n2, num2)
        widget_change(lbl_operator, operator)
        
        # Change the text of the reset button
        start_reset_btn.configure(text = 'START')
            
        # Reset score
        reset_score()
        
        # Reset stopwatch
        reset_stopwatch()
        
        # Make clicked_start false 
        clicked_start = False
        
        # Make entry box for the answer to the flash cards disabled
        ans.configure(state = 'disabled')
        
        # Make the number of questions entry box open
        num_of_questions.configure(state = 'normal')
    else:
        # Focus cursor on entry box where user can answer the math flash cards
        ans.focus()
        
        # Set time_ticking to false as stopwatch has stopped
        time_ticking = False
        
        # Call on function to validate the number of questions
        get_num_of_q()
    
        # Call on function to validate the level
        get_level()
        
        # Check that the level and the number of questions the user entered is
        # correct
        if valid_num_of_q and valid_level:
            # Make entry box for answer to the flash cards open 
            ans.configure(state = 'normal')
        
            # Change the text of the start button to reset
            start_reset_btn.configure(text = 'RESET')

            # Call a function to change the math flash cards
            change_question()

            # Start the stopwatch
            start_stopwatch()

            # Make clicked_start true
            clicked_start = True
            
            # Make the number of questions entry box readonly so user can not
            # change the number of questions until the progress bar is filled
            num_of_questions.configure(state = 'readonly')
            
            
        # Reset the score
        reset_score()

# function that calls on other functions to change the operator, get the level
# and change the numbers in the question depending on the level
# input: none
# returns: nothing
def change_question():
    # Call on global variable
    global level
    
    # Get the level the user chose
    get_level()
    
    # Change the operator
    change_operator()
    
    # Depending on the level generate random numbers
    if level == 1:
        random_numbers(1, 3)
    elif level == 2:
        random_numbers(1, 6)
    elif level == 3:
        random_numbers(1, 9)
    elif level == 4:
        random_numbers(1, 12)

# function that adds to the progressbar
# input: none
# returns: nothing
def progressbar():
    
    # Call on global variables
    global num_q_first_selection, counter, increment
    
    # Check if given input is positive and an integer
    if num_q_first_selection > 0 and num_q_first_selection == \
       int(num_q_first_selection) and valid_level:
        
        # Check if the next counter increment will equal the num of questions
        # entered at the start
        if counter + 1 == num_q_first_selection:
            
            # Find the increment to split the progress bar evenly
            increment = 100 // num_q_first_selection
            
            # If the increment is not a factor of 100 make the last increment
            # everything that is remaining 
            if increment * counter != 0:
                if 100 % (increment * counter) != 0:
                    increment = 100 % (increment * counter)
        else:
            # Increment evenly as long as possible
            increment = 100 // num_q_first_selection
            
        # Increase the progress
        bar['value'] = int(bar['value']) + increment
        
        # Check if the progressbar is completely filled
        if bar['value'] >= 100:
            # If it is reset the counter and increment
            counter = 0
            increment = 0
        else:
            counter += 1

# function to get the answer the user inputs
# input: none
# returns: nothing
def ans_num():
    # Call on a global variable
    global ans_valid
    
    # Get the answer the user entered 
    answer = ans.get()

    # Check if answer data type is valid
    try:
        if int(answer):
            ans_valid = True
    except:
        ans_valid = False
        print()
    return answer

# function to check if the user's answer is correct
# input: none
# returns: nothing
def check_ans():
    # Call on global variables
    global num1, num2, incorrect, correct, total, operator, img, \
           valid_num_of_q, valid_level, num_q_first_selection, clicked_start, \
           counter2, ans_valid
    
    # Initialize local variables needed for the function
    actual_ans = 0
    answer = 1
    box = '✅'
    ans_correct_or_incorrect = 1
    
    # Get the answer the user entered by calling a function
    try:
        # Get the answer and convert it to an integer
        answer = int(ans_num())
    except:
        print()

    # Add clicked_start so that the user is forced at first play of the game to
    # press start instead of go
    if clicked_start:
        # Make entry box for the answer to the flash cards open
        ans.configure(state = 'normal')
        
        # Get the level
        get_level()
        
        # Check the answer to the flash cards
        if (ans_valid or answer == 0) and valid_level and valid_num_of_q:
            if num1 != 0:
                if operator == '+':
                    # Set actual answer
                    actual_ans = num1 + num2
                    
                    # Check if user answer is correct
                    if num1 + num2 == answer:
                        # If user answer is correct set variable to 1 to
                        # indicate that answer is correct
                        ans_correct_or_incorrect = 1
                    else:
                        # If user answer is incorrect set variable to -1 to
                        # indicate that answer is incorrect
                        ans_correct_or_incorrect = -1
                elif operator == '-':
                    # Set actual answer
                    actual_ans = num1 - num2
                    
                    # Check if user answer is correct
                    if num1 - num2 == answer:
                        # If user answer is correct set variable to 1 to
                        # indicate that answer is correct
                        ans_correct_or_incorrect = 1
                    else:
                        # If user answer is incorrect set variable to -1 to
                        # indicate that answer is incorrect
                        ans_correct_or_incorrect = -1
                elif operator == '÷':
                    # Set actual answer
                    actual_ans = num1 // num2
                    
                    # Check if user answer is correct
                    if num1 // num2 == answer:
                        # If user answer is correct set variable to 1 to
                        # indicate that answer is correct
                        ans_correct_or_incorrect = 1
                    else:
                        # If user answer is incorrect set variable to -1 to
                        # indicate that answer is incorrect
                        ans_correct_or_incorrect = -1
                else:
                    if operator == 'x':
                        # Set actual answer
                        actual_ans = num1 * num2
                        
                        # Check if user answer is correct
                        if num1 * num2 == answer:
                            # If user answer is correct set variable to 1 to
                            # indicate that answer is correct
                            ans_correct_or_incorrect = 1
                        else:
                            # If user answer is incorrect set variable to -1 to
                            # indicate that answer is incorrect
                            ans_correct_or_incorrect = -1
                        
                # Correspondingly adjust the score and an image
                if ans_correct_or_incorrect == 1:
                    correct += 1
                    img = 'correctanswer.png'
                    image.configure(file = img)
                    lbl_caption.configure(text = 'CORRECT!')
                elif ans_correct_or_incorrect == -1:
                    incorrect += 1
                    img = 'incorrectanswer.png'
                    image.configure(file = img)
                    lbl_caption.configure(text = 'INCORRECT!')
                    box = '❌'
                    
                if ans_correct_or_incorrect == 1 or ans_correct_or_incorrect \
                   == -1:
                    
                    # Add to the total attempts
                    total += 1
                    
                    # Add to the copy of total
                    counter2 += 1
                    
                    # Add the question to the question log
                    previous_questions.insert(INSERT, box + ' ' + str(num1) + \
                                              ' ' + operator + ' ' + str(num2) \
                                              + ' = ' + str(actual_ans) + \
                                              ' | Your answer: ' + str(answer) \
                                              + '\n')
                    
                    # Change the question
                    change_question()
                
                    # Increase progress
                    progressbar()
            
            # Clear the answer the user entered in the entry box 
            ans.delete(0, 'end')
        else:
            if num1 == 0:
                # Get the new amount of questions the user entered
                get_num_of_q()
                
                # Continue playing if level and number of questions are valid
                if valid_level and valid_num_of_q:
                    # Reset and start the stopwatch again by calling a function
                    reset_start_stopwatch()
                    
                    # Hide the image and its caption
                    img = 'blankimage.png'
                    image.configure(file = img)
                    lbl_caption.configure(text = '')
                    
                    # Reset the progressbar
                    bar['value'] = 0
                    
                    # Display a new question
                    change_question()
                    
                    # Lock the number of questions so they can not be changed
                    num_of_questions.configure(state = 'readonly')
            else:
                # If answer entered is not a number give an error message
                if not ans_valid:
                    messagebox.askokcancel('Error!', 'Please enter a number!')

        # Call on a function to configure the score
        widget_change(lbl_correct_num, correct)
        widget_change(lbl_incorrect_num, incorrect)
        widget_change(lbl_total_num, total)

    # To indicate that the number of questions have been reached reset the flash
    # cards
    if counter2 == num_q_first_selection:
        # Focus the cursor on the entry box asking for number of questions
        num_of_questions.focus()
        
        # Reset the flash cards to show the starting screen
        num1, num2, operator = 0, 0, '?'
        widget_change(lbl_n1, num1)
        widget_change(lbl_n2, num2)
        widget_change(lbl_operator, operator)
        
        # Pause stopwatch after progress bar is filled
        pause_time()
        
        # Give congratulations message
        message_complete = '''You have completed your questions. You now have
the option to change the number of questions and other settings or you can
continue playing by clicking Go!'''
        messagebox.askokcancel('Congratulations', message_complete)
        
        # Reset counter2
        counter2 = 0
        
        # Make entry box for the answer to the flash cards disabled
        ans.configure(state = 'disabled')
        
        # Make the number of questions entry box open
        num_of_questions.configure(state = 'normal')

################################################################################
# Main program

# Initialize variables
num1 = 0
num2 = 0
operator = '?'
valid_num_of_q = False
valid_level = False
num_q_first_selection = 0.1
counter = 0
clicked_start = False
incorrect = 0
correct = 0
total = 0
level = 0
counter2 = 0
increment = 0.0
time_ticking = False
hours, minutes, seconds = 0, 0, 0
add_time = 0
ans_valid = False
mem_message = 'Where you make your memory stronger'
instructions = ''' Flash cards are here to build up your arithmetic skills.
In the next tab you will be given random math flash cards based upon your
selected difficulty and number of questions. You will also have the option to
include negative numbers.
 
GOOD LUCK and happy solving!
'''
level_info = '''
Level
1
2
3
4
'''
num_range_info = '''
Number Range(inclusive)
1-3
1-6
1-9
1-12
'''
operator_info = '''
Operator
+, -, x
+, -, x
+, -, x
+, -, x
'''
note = '''
Note: changing the number of questions in the middle of the game will not have
any effect until the progress bar is completed.  
'''
pady_question_row = 150
img = ''

# Create main window
window = Tk()
window.title('Flash Cards')
window.geometry('1024x768')

# Create tabs
tab_control = ttk.Notebook(window)

# Create instructions tab
tab_instructions = Frame(tab_control, bg = 'aquamarine4')
tab_control.add(tab_instructions, text = 'Instructions📄')

# Create flash cards tab
tab_flash_cards = Frame(tab_control, bg = 'aquamarine4')
tab_control.add(tab_flash_cards, text = 'Flash Cards')

# Create a tab containing all the previous questions and responses
tab_log = Frame(tab_control, bg = 'aquamarine4')
tab_control.add(tab_log, text = 'Question Log')

# Pack tabs
tab_control.pack(expand = 1, fill = 'both')

# Buttons

# Create buttons

# Create a button that will check if the entered answer is correct
check_ans_btn = Button(tab_flash_cards, text = 'Go!', width = 10, \
                       font = ('KG Midnight Memories', 15), command = check_ans)

# Create start/reset button
start_reset_btn = Button(tab_flash_cards, text='START', width = 11, \
                   font = ('KG Midnight Memories', 14), command = start_reset, \
                   bg = 'GhostWhite')

# Place buttons

# Place a button that will check if the entered answer is correct
# Used .place instead of .grid to put the button at the bottom right corner.
# Using grid messed up the formatting and it made it difficult to left align.
check_ans_btn.place(x = 810, y = 580)

# Place start/reset button
start_reset_btn.grid(row = 9, column = 2, pady = 20)

# Content for instructions tab

# Create empty labels
lbl_empty1 = Label(tab_instructions, text='', padx = 70, bg = 'aquamarine4')
lbl_empty2 = Label(tab_instructions, text='', pady = 20, bg = 'aquamarine4')

# Create a heading label
lbl_heading_instructions = Label(tab_instructions, text = '''Welcome to Hetav\'s
Flash Cards''', pady = 10, font = ('KG Midnight Memories', 15), bg = \
                                 'aquamarine4', fg = 'GhostWhite')

# Create a memorable message
lbl_memorable = Label(tab_instructions, text = mem_message, font = \
                      ('KG Midnight Memories', 15), bg = 'aquamarine4', fg = \
                      'GhostWhite')

# Create a label containing instructions to the game
lbl_instructions = Label(tab_instructions, text = instructions, font = \
                         ('KG Midnight Memories', 15), bg = 'aquamarine4', \
                         fg = 'GhostWhite')

# Create the labels containing information about the levels
lbl_level_info = Label(tab_instructions, text = level_info, font = \
                         ('KG Midnight Memories', 16), bg = 'aquamarine4', \
                       fg = 'GhostWhite')
lbl_num_range_info = Label(tab_instructions, text = num_range_info, font = \
                         ('KG Midnight Memories', 16), bg = 'aquamarine4', \
                           fg = 'GhostWhite')
lbl_operator_info = Label(tab_instructions, text = operator_info, font = \
                         ('KG Midnight Memories', 16), bg = 'aquamarine4', \
                          fg = 'GhostWhite')

# Place the empty labels for spacing
lbl_empty1.grid(row = 0, column = 0, columnspan = 3)
lbl_empty2.grid(row = 2, column = 3, columnspan = 3)

# Place the heading label
lbl_heading_instructions.grid(row = 0, column = 3)

# Place the memorable message
lbl_memorable.grid(row = 1, column = 3)

# Place the label containing instructions to the game
lbl_instructions.grid(row = 3, column = 3)

# Place the labels containing information about the levels
lbl_level_info.grid(row = 5, column = 2)
lbl_num_range_info.grid(row = 5, column = 3)
lbl_operator_info.grid(row = 5, column = 4)

# Content for flash_cards tab

# Create progress bar
bar = Progressbar(tab_flash_cards, length = 100, style = \
                  'aquamarine4.Horizontal.TProgressbar')
bar['value'] = 0

# Create labels for question
lbl_n1 = Label(tab_flash_cards, text = num1, \
               pady = pady_question_row, font = ('KG Midnight Memories', 45), \
               bg = 'aquamarine4', fg = 'GhostWhite')
lbl_n2 = Label(tab_flash_cards, text = num2, \
               pady = pady_question_row, font = ('KG Midnight Memories', 45), \
               bg = 'aquamarine4', fg = 'GhostWhite')
lbl_operator = Label(tab_flash_cards, text = operator, \
                     pady = pady_question_row, font = \
                     ('KG Midnight Memories', 45), bg = 'aquamarine4', fg = \
                     'GhostWhite')
lbl_equal = Label(tab_flash_cards, text = '=', \
                  pady = pady_question_row, font = \
                  ('KG Midnight Memories', 45), bg = 'aquamarine4', \
                  fg = 'GhostWhite')
ans = Entry(tab_flash_cards, width = 6, state = 'disabled', font = \
            ('KG Midnight Memories', 45))

# Create empty labels
empty_3 = Label(tab_flash_cards, text='', pady = 80, bg = 'aquamarine4')
empty_4 = Label(tab_flash_cards, text='', padx = 65, bg = 'aquamarine4')
empty_5 = Label(tab_flash_cards, text='', padx = 65, bg = 'aquamarine4')
empty_6 = Label(tab_flash_cards, text='', padx = 65, bg = 'aquamarine4')

# Create the label called Settings
lbl_settings = Label(tab_flash_cards, text = 'Settings', font = \
                     ('KG Midnight Memories', 15), bg = 'aquamarine4', fg = \
                     'GhostWhite')

# Create a label indicating number of questions to ask
lbl_num_of_questions = Label(tab_flash_cards, text = 'How many questions:', \
                             font = ('KG Midnight Memories', 15), padx = 30, \
                             bg = 'aquamarine4', fg = 'GhostWhite')

# Using an entry class create an area where the user can indicate how many
# questions to ask
num_of_questions = Entry(tab_flash_cards, width = 5, font = \
                         ('KG Midnight Memories', 20), bg = 'GhostWhite')

# Create the labels and the radio buttons that ask to include negative numbers
selected_neg_num = IntVar()
lbl_neg_num = Label(tab_flash_cards, text = 'Include negative numbers?', \
                    font = ('KG Midnight Memories', 15), pady = 14, bg = \
                    'aquamarine4', fg = 'GhostWhite')
rad_yes_neg = Radiobutton(tab_flash_cards, text = 'Yes', value = 1, \
                      variable = selected_neg_num, font = \
                          ('KG Midnight Memories', 15), bg = 'aquamarine4')
rad_no_neg = Radiobutton(tab_flash_cards, text = 'No', value = 0, \
                     variable = selected_neg_num, font = \
                         ('KG Midnight Memories', 15), bg = 'aquamarine4')

# Create the labels and the radio buttons that ask to include division
selected_division = IntVar()
lbl_division_operator = Label(tab_flash_cards, text = 'Include Division?', \
                              font = ('KG Midnight Memories', 15), pady = 14, \
                              bg = 'aquamarine4', fg = 'GhostWhite')
rad_yes_division = Radiobutton(tab_flash_cards, text = 'Yes', value = 1, \
                      variable = selected_division, font = \
                               ('KG Midnight Memories', 15), bg = 'aquamarine4')
rad_no_division = Radiobutton(tab_flash_cards, text = 'No', value = 0, \
                     variable = selected_division, font = \
                              ('KG Midnight Memories', 15), bg = 'aquamarine4')

# Create the image and its caption
lbl_caption = Label(tab_flash_cards, text = '', \
                    font = ('KG Midnight Memories', 15), bg = 'aquamarine4')
image = PhotoImage(file = img)
lbl_img = Label(tab_flash_cards, image = image, bg = 'aquamarine4')

# Create the label asking to select level
lbl_level = Label(tab_flash_cards, text = 'Select Level', \
                  font = ('KG Midnight Memories', 15), bg = 'aquamarine4', \
                  fg = 'GhostWhite')

# Create the SpinBox that gives the user an option to choose their level
spin_level = Spinbox(tab_flash_cards, from_ = 1, to = 4, width = 5, \
                     font = ('KG Midnight Memories', 20), bg = 'GhostWhite')

# Create the labels that contain the score
lbl_score = Label(tab_flash_cards, text = 'Score', font = \
                  ('KG Midnight Memories', 18), bg = 'aquamarine4', fg = \
                  'GhostWhite')
lbl_incorrect = Label(tab_flash_cards, text = 'Wrong:', font = \
                      ('KG Midnight Memories', 18), bg = 'aquamarine4', fg = \
                      'GhostWhite')
lbl_incorrect_num = Label(tab_flash_cards, text = incorrect, \
                          font = ('KG Midnight Memories', 18), bg = \
                          'aquamarine4', fg = 'GhostWhite')
lbl_correct = Label(tab_flash_cards, text = 'Correct:', font = \
                    ('KG Midnight Memories', 18), bg = 'aquamarine4', \
                    fg = 'GhostWhite')
lbl_correct_num = Label(tab_flash_cards, text = correct, font = \
                        ('KG Midnight Memories', 18), bg = 'aquamarine4', \
                        fg = 'GhostWhite')
lbl_total = Label(tab_flash_cards, text = 'Total Attempts:', \
                  font = ('KG Midnight Memories', 18), bg = 'aquamarine4', \
                  fg = 'GhostWhite')
lbl_total_num = Label(tab_flash_cards, text = total, font = \
                      ('KG Midnight Memories', 18), bg = 'aquamarine4', \
                      fg = 'GhostWhite')

# Create a label for the stopwatch
lbl_stopwatch = Label(tab_flash_cards, text='00:00:00', font = \
                  ('KG Midnight Memories', 15), bg = 'aquamarine4')

# Place progress bar
bar.grid(row = 0, column = 0, rowspan = 2, columnspan = 13, sticky = W + E)

# Place widgets containing the question
# Used .place instead of .grid to relatively center the question on the screen
lbl_n1.place(x = 100, y = 415)
lbl_n2.place(x = 340, y = 415)
lbl_operator.place(x = 220, y = 415)
lbl_equal.place(x = 470, y = 415)
ans.place(x = 580, y = 565)

# Place empty labels
empty_3.grid(row = 20, column = 7)
empty_4.grid(row = 4, column = 6)
empty_5.grid(row = 5, column = 6)
empty_6.grid(row = 6, column = 6)

# Place a label called Settings
lbl_settings.grid(row = 2, column = 2)

# Place the label indicating number of questions to ask
lbl_num_of_questions.grid(row = 3, column = 0)

# Place the entry box asking for number of questions
num_of_questions.grid(row = 4, column = 0)

# Focus the cursor on the entry box asking for number of questions when the
# window loads
num_of_questions.focus()

# Place the labels and the radio buttons that ask to include negative numbers
lbl_neg_num.grid(row = 3, column = 3, columnspan = 3)
rad_yes_neg.grid(row = 4, column = 3, columnspan = 2)
rad_no_neg.grid(row = 4, column = 4, columnspan = 2)

# Place the labels and the radio buttons that ask to include division
lbl_division_operator.grid(row = 6, column = 3, columnspan = 3)
rad_yes_division.grid(row = 7, column = 3, columnspan = 2)
rad_no_division.grid(row = 7, column = 4, columnspan = 2)

# Place the image and its caption
# Used .place instead of .grid as it was difficult to format with .grid
lbl_caption.place(x = 520, y = 350)
lbl_img.place(x = 670, y = 340)

# Place the label asking to select level
lbl_level.grid(row = 6, column = 0)

# Place the SpinBox that gives the user an option to choose their level
spin_level.grid(row = 7, column = 0)

# Place the labels containing the score
lbl_score.grid(row = 3, column = 7, columnspan = 2)
lbl_incorrect.grid(row = 4, column = 7)
lbl_incorrect_num.grid(row = 4, column = 8, columnspan = 5)
lbl_correct.grid(row = 5, column = 7)
lbl_correct_num.grid(row = 5, column = 8, columnspan = 5)
lbl_total.grid(row = 6, column = 7)
lbl_total_num.grid(row = 6, column = 8, columnspan = 5)

# Place the label for the stopwatch
lbl_stopwatch.grid(row = 21, column = 8, columnspan = 1)

# Contents of the Question Log tab

# Create the label for the header
lbl_heading_log = Label(tab_log, text = \
                        'The previous questions and answers are:', font = \
                        ('KG Midnight Memories', 18) , pady = 15, padx = 345, \
                        fg = 'GhostWhite', bg = 'aquamarine4')

# Create a ScrolledText Widget
previous_questions = scrolledtext.ScrolledText(tab_log, width = 50, height = 30)

# Place the label for the header
lbl_heading_log.grid(row = 0, column = 2, columnspan = 3, sticky = W + E)

# Place the ScrolledText Widget
previous_questions.grid(row = 1, column = 3)

# Keep window open
window.mainloop()
