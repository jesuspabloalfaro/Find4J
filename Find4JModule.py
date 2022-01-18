import csv
import sys
import nmap

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
        nm.scan(hosts=ip, arguments='sV -sC')
        return nm, ip, ports

    def compare_data(self, product):
        """ Function to compare found products with that of known log4j vulnerabilities """
        with open("vuln.csv", 'r') as f:
            reader = csv.reader(f, delimiter="\n")
            for vuln in reader:
                if str(product) in str(vuln):
                    return True

    def print_scan_data(self, scan):
        """ Function to print product scan data """
        nm, ip, port = scan
        vulnerable = []
        ports = nm[ip]['tcp'].keys()
        for host in nm.all_hosts():
            for port in ports:
                product = nm[host]['tcp'][port]['product']
                if self.compare_data(product):
                    vulnerable.append([host, product])

    def output_scan_data():
        """ Function to output scan data to csv """
        raise NotImplementedError
