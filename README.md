# Illumio-Coding-Assignment
Illumio Coding Assignment 2019-2020, PCE teams

Host-Based Firewall written in Python and compiled using Python3

## USER GUIDE
### 1) Set-up
Clone this repository and change your directory into this folder.
### 2) Run the python interactive shell
Using the command `python3`, start the python interactive shell.
### 3) Run the program
Start the program using the following lines in the interactive shell:

`from Firewall import Firewall`

`fw = Firewall('input.csv')`

Ensure that the input file for the rules is in the same directory as *Firewall.py*.
### 4) Query the program
Enter query in the format: fw.accept_packet(direction, protocol, port, ip_address):

- direction (string): “inbound” or “outbound”
- protocol (string): exactly one of “tcp” or “udp”, all lowercase
- port (integer) – an integer in the range [1, 65535]
- ip_address (string): a single well-formed IPv4 address.

## OVERVIEW OF DESIGN AND CONSIDERATION
###Tables
4 tables are used to store information based on an IP-address and a corresponding Port number
The 4 tables are grouped acccording to the possible combinations of direction and protocol.

![decision tree](/diagram.png)
