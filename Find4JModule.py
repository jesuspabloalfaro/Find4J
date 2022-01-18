import sys
import nmap
import pprint

class IntOutOfBounds(Exception):
    pass

class PortOutOfBounds(Exception):
    pass

class Find4JClass():
    def banner():
        """ Banner for Find4J """
        print(""" 
______ _           _   ___    ___ 
|  ___(_)         | | /   |  |_  |
| |_   _ _ __   __| |/ /| |    | |
|  _| | | '_ \ / _` / /_| |    | |
| |   | | | | | (_| \___  |/\__/ /
\_|   |_|_| |_|\__,_|   |_/\____/ 
                                                           
""")
        print("Find4J is a Python script to find applications potentially vulnerable to log4j.")
        print("Developed By: Jesus-Pablo Alfaro")
        print("Based on Python-Nmap\n")

    def create_scan(ip, ports):
        """ Function to create scan with user inputs """
        nm = nmap.PortScanner()  
        nm.scan(ip, ports)
        print(nm.scaninfo())

    def output_scan_data():
        """ Function to output scan data to csv """
        raise NotImplementedError
