# Flash Cards Math Game

A comprehensive Python GUI application that helps users practice and improve their arithmetic skills through interactive flash cards. Built with Tkinter, this educational tool provides a fun and engaging way to master mathematical operations.

## 📋 Overview

This Flash Cards application generates random math problems based on user-selected difficulty levels and settings. It features a complete learning environment with progress tracking, timing capabilities, and detailed question logging to help users monitor their mathematical progress.

## ✨ Features

### Core Functionality
- **Random Math Problems**: Generates arithmetic problems using addition (+), subtraction (-), multiplication (×), and division (÷)
- **Multiple Difficulty Levels**: 4 levels with increasing number ranges
- **Customizable Settings**: User-defined number of questions, negative numbers inclusion, and division problems
- **Real-time Scoring**: Tracks correct/incorrect answers and total attempts
- **Progress Tracking**: Visual progress bar showing completion status

### Advanced Features
- **Integrated Stopwatch**: Times your practice sessions with start/pause/reset functionality
- **Question History Log**: Comprehensive log of all previous questions, answers, and results
- **Visual Feedback**: Immediate visual confirmation of correct/incorrect answers with images
- **Input Validation**: Robust error handling for all user inputs
- **Tabbed Interface**: Clean, organized UI with Instructions, Flash Cards, and Question Log tabs

### Educational Benefits
- **Adaptive Learning**: Different difficulty levels accommodate various skill levels
- **Memory Enhancement**: "Where you make your memory stronger" - focused on building mathematical confidence
- **Performance Analytics**: Detailed scoring system to track improvement over time

## 🎮 How to Play

### Getting Started
1. **Launch the Application**: Run the main Python file
2. **Read Instructions**: Check the Instructions tab for complete game rules and level information
3. **Configure Settings**:
   - Set number of questions (1-100)
   - Choose difficulty level (1-4)
   - Decide whether to include negative numbers
   - Select whether to include division problems

### Playing the Game
1. **Click START**: Begin your practice session
2. **Answer Questions**: Type your answers in the input field
3. **Submit Answers**: Click "Go!" or press Enter
4. **Track Progress**: Monitor your score and progress bar
5. **Review Performance**: Check the Question Log tab for detailed history

### Game Controls
- **START/RESET Button**: Begins new session or resets current game
- **Go! Button**: Submits your answer
- **Stopwatch**: Automatically tracks your session time
- **Progress Bar**: Shows completion percentage

## 🎯 Difficulty Levels

| Level | Number Range | Operators Available |
|-------|-------------|-------------------|
| 1     | 1-3         | +, -, × (and ÷ if enabled) |
| 2     | 1-6         | +, -, × (and ÷ if enabled) |
| 3     | 1-9         | +, -, × (and ÷ if enabled) |
| 4     | 1-12        | +, -, × (and ÷ if enabled) |

### Required Python Modules
```python
tkinter          # GUI framework
tkinter.ttk      # Enhanced GUI widgets
random           # Random number generation
```

## 🚀 Installation & Setup

### Quick Start
1. **Download Files**: Ensure you have all project files in the same directory
2. **Check Python**: Verify Python 3.6+ is installed
3. **Run Application**:
   ```bash
   python HP-FlashCards.py
   ```

### File Structure
```
FlashCardsGame/
├── HP-FlashCards.py              # Main application (full version)
├── HP-FlashCardsStep2ScreenOnly.py  # Screen-only version (demo)
├── blankimage.png                       # Placeholder image
├── correctanswer.png                    # Correct answer feedback image
├── incorrectanswer.png                  # Incorrect answer feedback image
├── kg_midnight_memories.zip             # Font package
└── README.md                           # This documentation
```

## 📊 User Interface

### Tab Navigation
- **Instructions📄**: Game rules, level information, and helpful tips
- **Flash Cards**: Main game interface with problem display and controls
- **Question Log**: Complete history of all attempted questions and results

### Main Game Screen Layout
- **Progress Bar**: Top of screen, shows completion status
- **Question Display**: Large, centered math problem
- **Answer Input**: Text field for user responses
- **Settings Panel**: Level selection, question count, and options
- **Score Panel**: Real-time tracking of correct/incorrect/total attempts
- **Stopwatch**: Session timer in bottom corner

## 📈 Progress Tracking

### Scoring System
- **Correct Answers**: Running count of successful responses
- **Wrong Answers**: Track of mistakes for improvement focus  
- **Total Attempts**: Complete question count for session statistics
- **Percentage Calculation**: Easy mental math to track success rate

### Session Management
- **Stopwatch Integration**: Automatic timing for performance analysis
- **Progress Bar**: Visual representation of completion status
- **Question Logging**: Permanent record of all attempts with timestamps

## 🔧 Advanced Features

### Input Validation
- **Number Range Validation**: Ensures question count is between 1-100
- **Level Validation**: Confirms selected level is 1-4
- **Answer Type Checking**: Validates numeric input for math answers
- **Error Messages**: Clear, helpful feedback for invalid inputs

### Smart Question Generation
- **Division Logic**: Ensures division problems result in whole numbers
- **Negative Number Handling**: Intelligent placement of negative signs
- **Operator Distribution**: Random but balanced selection of math operations
- **Difficulty Scaling**: Numbers scale appropriately with selected level

### Session Control
- **Start/Reset Functionality**: Clean session management
- **Mid-Game Settings**: Locked settings during active sessions
- **Completion Handling**: Automatic session end with congratulatory message
- **Continue Option**: Seamless transition to new sessions

## 📚 Educational Applications

### Classroom Use
- **Individual Practice**: Self-paced learning for students
- **Skill Assessment**: Teachers can monitor student progress
- **Homework Tool**: Engaging alternative to traditional worksheets
- **Math Centers**: Perfect for rotating activity stations

### Home Learning
- **Parent-Child Activity**: Collaborative learning experience
- **Daily Practice**: Short sessions to maintain math skills
- **Progress Monitoring**: Parents can track improvement over time
- **Confidence Building**: Positive reinforcement through visual feedback


**Happy Learning! 🎓✨**  
*"Where you make your memory stronger"*
