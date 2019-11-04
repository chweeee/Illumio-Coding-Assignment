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

### Query Processing
![decision tree](/diagram.PNG)

Using this tree to locate the correponding table for each Query, each query is evaluated by querying from the table.

### Tables
4 tables are used to store information based on an IP-address and a corresponding Port number
The 4 tables are grouped acccording to the possible combinations of direction and protocol.

In each table, the key is the IP-address and the value is a list of port numbers associated with the IP address

### Space and Time complexity

At worst case scenario, the space complexity for each table will be 2^32(total no of IPv4 addresses) * 65535 (total number of ports) * 4(4 tables)

Time complexity for querying: locating the IPv4 Address [O(1)] + finding the port [O(n), where n is the number of ports associated with IPv4 address]

Initialising of table only happens once (at the start of the program), so operations with the largest complexity should happen there.
Assuming that we want to have short query times, to maximise efficiency of the Firewall, the trade-off for a quicker time to evaluate query for a larger storage space is justified.

## Testing

I focused mainly on the correctness of the tables, and any rules can fall into any 1 of 4 categories:

case 1: sinlge port number + sinlge ip addr
case 2: port range + sinlge ip addr
case 3: sinlge port number + ip range
case 4: port range + ip range

Tests used (input.csv) were mostly to cover these 4 cases to ensure that the tables are populated properly.

