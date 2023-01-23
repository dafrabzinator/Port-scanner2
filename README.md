## PORT SCANNER
A simple, multi-threaded port scanner written in Python.
## Usage
`python port_scanner.py [ip] [options]`
## Options
`--start-port: Starting port to scan (default: 1)`
`--end-port: Ending port to scan (default: 1000)`
--timeout: Connection timeout (default: 1)`
## Example
`python port_scanner.py 192.168.1.1 --start-port 1 --end-port 1000 --timeout 1`
This command will scan all ports from 1 to 1000 on the IP address 192.168.1.1, with a timeout of 1 second for each connection attempt.

## Note
This script is for educational and testing purposes only. Before using this script, it is important to obtain explicit consent from the owner of the targeted system. Use at your own risk.
