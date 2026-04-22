#!/bin/bash

while true
do
clear

# Banner
figlet "SAHIL NIKAM" | lolcat

# Menu (App style box)
choice=$(dialog --clear \
--title "OSINT TOOL MENU" \
--menu "Select Option" 15 50 6 \
1 "Domain Info" \
2 "IP Lookup" \
3 "Username Search" \
4 "Exit" \
2>&1 >/dev/tty)

clear

case $choice in
  1)
    read -p "Enter domain: " domain
    whois $domain
    read -p "Press enter to go back..."
    ;;
    
  2)
    read -p "Enter IP: " ip
    curl ipinfo.io/$ip
    read -p "Press enter to go back..."
    ;;
    
  3)
    read -p "Enter username: " user
    echo "Instagram: https://instagram.com/$user"
    echo "GitHub: https://github.com/$user"
    echo "Twitter: https://twitter.com/$user"
    read -p "Press enter to go back..."
    ;;
    
  4)
    exit
    ;;
    
  *)
    echo "Invalid option"
    ;;
esac

done
