# Port-scanner2
this script scan Nasa's Ip address . for educational purpose only!
## Usage
Download or clone my repository `git clone https;github.com/dafrabs/Port-scanner2.git`

run the script directly on your terminal using:

`python3 port_scanner.py [ip] [options]`

## Options
`--start-port: Starting port to scan (default: 1)`
`--end-port: Ending port to scan (default: 1000)`
--timeout: Connection timeout (default: 1)`
## Example
`python port_scanner.py 192.168.1.1 --start-port 1 --end-port 1000 --timeout 1`
This command will scan all ports from 1 to 1000 on the IP address 192.168.1.1, with a timeout of 1 second for each connection attempt.

## Note
This script is for educational and testing purposes only. Before using this script, it is important to obtain explicit consent from the owner of the targeted system. Use at your own risk.
