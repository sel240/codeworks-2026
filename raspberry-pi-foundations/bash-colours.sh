#!/bin/bash

# Clear the screen for a clean start
clear
echo "=================================================="
echo "               STROOP EFFECT TEST"
echo "=================================================="
echo "Instructions: Type the COLOR of the word, NOT the word itself!"
echo "Options to type: red, green, yellow, blue, magenta, cyan"
echo "=================================================="
echo ""

# Define text colors using ANSI escape sequences
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
MAGENTA='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
RESET='\e[0m'

# Arrays for color names and their matching ANSI variables
words=("RED" "GREEN" "YELLOW" "BLUE" "MAGENTA" "CYAN" "WHITE")
colors=("$RED" "$GREEN" "$YELLOW" "$BLUE" "$MAGENTA" "$CYAN" "$WHITE")
color_names=("red" "green" "yellow" "blue" "magenta" "cyan" "white"
)

score=0
total_rounds=25

for ((i=1; i<=total_rounds; i++)); do
    # Generate two different random indexes to ensure word and color are mismatched
    word_idx=$((RANDOM % 7))
    color_idx=$((RANDOM % 7))
    while [ $word_idx -eq $color_idx ]; do
        color_idx=$((RANDOM % 7))
    done

    # Get the target correct answer (the color of the ink)
    correct_answer="${color_names[$color_idx]}"

    # Display the current round and the colored word
    echo -e "Round $i/$total_rounds: What color is this word?"
    echo -e "       ${colors[$color_idx]}${words[$word_idx]}${RESET}"
    
    # Prompt user for input
    read -p "Your answer: " user_input
    
    # Convert input to lowercase to prevent case-sensitive errors
    user_input=$(echo "$user_input" | tr '[:upper:]' '[:lower:]')

    # Check the answer
    if [ "$user_input" == "$correct_answer" ]; then
        echo -e "${GREEN}Correct!${RESET}\n"
        score=$((score + 1))
    else
        echo -e "${RED}Wrong!${RESET} The ink color was $correct_answer.\n"
    fi
    sleep 0.5
done

# Display final results
echo "=================================================="
echo "TEST COMPLETE!"
echo "Your Final Score: $score out of $total_rounds"
accuracy=$(( (score * 100) / total_rounds ))
echo "Accuracy: $accuracy%"
echo "=================================================="
read -p "Press Enter to exit..."
