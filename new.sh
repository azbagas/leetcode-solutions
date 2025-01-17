#! /usr/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Enter the solution name (topic/00-problem-name.py):${NC}"
read name

command=`cp template.py $name`

echo $command

echo -e "${GREEN}File created successfully. Happy solving!"