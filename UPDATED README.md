# Password Generator Tool - by Zabiullah

A simple and fast password generator tool for Termux users.

## Features
- Strong password generation
- Custom length option
- Easy to use

## Installation (Termux)

```bash
# Update and install required packages
pkg update && pkg upgrade
pkg install git -y
pkg install python -y

# Clone the tool from GitHub
git clone https://github.com/Zabiullah/password-generator  # <-- Replace with your real link

# Go to the tool folder
cd password-generator

# Run the tool
python password.py   # Or bash password.sh if it's a bash script
