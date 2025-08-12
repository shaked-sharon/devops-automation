#!/usr/bin/env python3

# Main program file
# Coordinates all files for automation tool


import json
import subprocess
import sys
import os
from src.machine import Machine
from src.logger import logger

def save_machines_to_config(machines):
    # This function saves the machine info to config file
    try:
        # Save as list of dicts
        config_data = {"virtual machine": [m.to_dict() for m in machines]}
        with open('configs/instances.json', 'w') as f:
            json.dump(config_data, f, indent=4)
        print(f"Saved {len(machines)} virtual machine(s) to config file")
        logger.info(f"Saved {len(machines)} virtual machine to instances.json")
        return True
    except Exception as e:
        print(f"Error saving configuration: {e}")
        logger.error(f"Failed to save configuration: {e}")
        return False

def load_machines_from_config():
    #Function loads machine info from config file
    try:
        if os.path.exists('configs/instances.json'):
            with open('configs/instances.json', 'r') as f:
                config_data = json.load(f)
                machines = config_data.get('virtual machine', [])
                return [Machine(**m) for m in machines]
        else:
            return []
    except Exception as e:
        print(f"Error loading configuration: {e}")
        logger.error(f"Failed to load configuration: {e}")
        return []

def provision_machines(machine_configs):
    # Function creates virtual machine / simulates provisioning
    provisioned_machines = []
    
    print("\n" + "="*50)
    print("Starting Infrastructure Provisioning...")
    print("="*50)
    
    for machine in machine_configs:
        print(f"\nProvisioning virtual machine: {machine.name}")
        print("-" * 30)
        if machine.provision():
            provisioned_machines.append(machine)
            print(f"Successfully provisioned {machine.name}")
        else:
            print(f"Failed to provision {machine.name}")
    return provisioned_machines

def provision_machine(machine):
    # Simulates provisioning
    logger.info(f"Provisioning virtual machine: {machine['name']}")
    # Simulates always successful
    return True
def install_services(machines):
    # Function simulates installation services on machines
    print("\n" + "="*50)
    print("Starting Service Installation...")
    print("="*50)
    
    for machine in machines:
        print(f"\nInstalling services on virtual machine: {machine.name}")
        print("-" * 40)
        try:
            script_path = 'scripts/call_nginx.sh'
            if not os.path.exists(script_path):
                raise FileNotFoundError(f"Script {script_path} not found")
            print(f"Running installation script for {machine.name}...")
            result = subprocess.run(
                ['bash', 'scripts/call_nginx.sh'],
                capture_output=True,
                text=True,
                check=True
            )
            if result.stdout:
                print("Installation script output:")
                print(result.stdout)
            if result.stderr:
                print("Installation script errors:")
                print(result.stderr)
            logger.info(f"Installation script ran successfully for {machine.name}")
            print(f"Installation script ran successfully for {machine.name}")
        except FileNotFoundError as e:
            error_msg = f"Installation script not found for {machine.name}: {e}"
            print(error_msg)
            logger.error(error_msg)
        except subprocess.CalledProcessError as e:
            error_msg = f"Failed installation for {machine.name}: {e}"
            print(error_msg)
            logger.error(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error installation for {machine.name}: {e}"
            print(error_msg)
            logger.error(error_msg)

def show_menu():
    #Function asks user what actions they want to take
    print("\n" + "="*50)
    print("DevOps Infrastructure Automation Program")
    print("="*50)
    print("1. Create new virtual machine")
    print("2. Show existing machines")
    print("3. Provision virtual machines")
    print("4. Install services to virtual machines")
    print("5. Full automation--Create, provision, install")
    print("6. Exit")
    print("-" * 50)

def show_existing_machines():
    # This function shows machines that are already saved
    machines = load_machines_from_config()
    if not machines:
        print("No virtual machines found for configuration.")
        return
    
    print("\nExisting virtual machines:")
    print("-" * 40)
    for i, machine in enumerate(machines, 1):
        print(f"{i}. Name: {machine.name}")
        print(f"   OS: {machine.os}")
        print(f"   CPU: {machine.cpu} cores")
        print(f"   RAM: {machine.ram} GB")
        print()

def main():
    # Main function that runs program
    print("Welcome to my DevOps Infrastructure Automation Program!")
    print("This program assists in creating and executing virtual machines.")
    
    # Ensures log directory exists
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    logger.info("DevOps Automation Program starting...")
    
    while True:
        show_menu()
        choice = input("Choose an option 1 - 6: ").strip()
        if choice == '1':
            # Create new machines
            print("\nCreating new virtual machine...")
            machines = []
            while True:
                print("Enter the details of the virtual machine (or type 'done' if you're finished):")
                name = input("Machine Name: ").strip()
                if name.lower() == 'done':
                    break
                os_type = input("Operating system (Ubuntu, CentOS, Windows, MacOS): ").strip()
                cpu = input("CPU cores (2 - 64): ").strip()
                ram = input("RAM in GB (1 - 128): ").strip()
                print()  # Add a blank line for readability
                try:
                    machine = Machine(name=name, os=os_type, cpu=int(cpu), ram=int(ram))
                    machines.append(machine)
                    print(f"Machine '{name}' successfully added! Hooray!")
                except Exception as e:
                    print(f"Input error: {e}")
                print("-" * 40)
            if machines:
                if save_machines_to_config(machines):
                    print("Virtual Machine(s) successfully created! Hooray!")
                else:
                    print("Error trying to save virtual machine...Boo!")
            else:
                print("No machine created. Sadface...")
        elif choice == '2':
            show_existing_machines()
        elif choice == '3':
            machines = load_machines_from_config()
            if machines:
                provision_machines(machines)
            else:
                print("No virtual machines found. Please create a virtual machine before continuing...")
        elif choice == '4':
            machines = load_machines_from_config()
            if machines:
                install_services(machines)
            else:
                print("No virtual machines found. Please create a virtual machine before continuing...")
        elif choice == '5':
            print("\nStarting automated process...")
            machines = []
            while True:
                print("Enter the details of the virtual machine (or type 'done' if you're finished):")
                name = input("Machine Name: ").strip()
                if name.lower() == 'done':
                    break
                os_type = input("Operating system (Ubuntu, CentOS, Windows, MacOS): ").strip()
                cpu = input("CPU cores (2 - 64): ").strip()
                ram = input("RAM in GB (1 - 128): ").strip()
                try:
                    machine = Machine(name=name, os=os_type, cpu=int(cpu), ram=int(ram))
                    machines.append(machine)
                    print(f"Machine '{name}' successfully added! Hooray!")
                except Exception as e:
                    print(f"Input error: {e}")
                print("-" * 40)
            if machines:
                if save_machines_to_config(machines):
                    provisioned_machines = provision_machines(machines)
                    install_services(provisioned_machines)
                    print("\nAutomation successfully completed! Hooray!")
                else:
                    print("Automation Error!! Could not save virtual machine...Boo!")
            else:
                print("No virtual machines created. Automation cancelled.")
        elif choice == '6':
            print("Thank you for using my DevOps Infrastructure Automation Program!")
            logger.info("DevOps Automation Program stopped")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
