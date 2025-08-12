# This file will be used to create a schema for the simulation of the virtual machines
# Each virtual machine should have a name, OS, cpu number, & ram number

import json
import logging

class Machine:
    # Function will run when I create a new machine
    def __init__(self, name, os, cpu, ram):
        # Stores the vm details that user inputs
        # Details needed for vm
        self.name = name
        self.os = os
        self.cpu = cpu  # int number i.e. 2,4,8, etc.
        self.ram = ram  # int number i.e. 2,4,8, etc.
    
    # Function turns vm details into dictionary
    # Note to self: Dictionary like a list with labels
    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }
    
    #Function simulates creating vm and writes log messages
    # If this was real, this would call API's
    def provision(self):
        # Prints messages simulating fake calling of vm
        print(f"Creating virtual machine: {self.name}")
        print(f"Operating System: {self.os}")
        print(f"CPU: {self.cpu} cores")
        print(f"RAM: {self.ram} GB")
        print(f"Virtual Machine {self.name} has successfully been created! Hooray!")
        
        # Will write  logfile that vm was simulated
        # Where log provisioning process should occur
        logging.basicConfig(filename='machine.log', level=logging.INFO)
        logging.info(f"Provisioned virtual machine: {self.name} - {self.os}, {self.cpu} CPU, {self.ram} GB RAM")
        
        return True
