#!/bin/bash

# Define an array of items to display
options=(Option1 off Option2 on Option3 off)

# Use whiptail to display the checkbox
whiptail --title "Checkbox example" --checklist \
"Choose options:" 15 50 5 "${options[@]}" 2> /tmp/choices

# Read the choices from the temp file and print them
choices=$(cat /tmp/choices)
echo "You chose: $choices"