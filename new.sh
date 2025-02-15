#! /usr/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Enter the solution name (topic/00-problem-name.py):${NC}"
read name

# Extract the topic folder from the input
topic_folder=$(dirname "$name")

# Check if the topic folder exists, if not, create it
if [ ! -d "$topic_folder" ]; then
    mkdir -p "$topic_folder"
    echo -e "${GREEN}Created folder: $topic_folder${NC}"
fi

# Copy the template to the new file
cp template.py "$name"

echo -e "${GREEN}File created successfully at $name. \nHappy solving!${NC}"