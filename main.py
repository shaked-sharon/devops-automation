#!/usr/bin/env python3

# Main program file
# Coordinates all files for automation tool

import json
import subprocess
import sys
import os

# Import our custom modules

from src.validation import validate_machine_input
from src.logger import logger
from src.validation import get_user_input

def save_machines_to_config(machines):
    # This function saves the machine information to our config file
    try:
        config_data = {"virtual machines": machines}
        with open('configs/instances.json', 'w') as f:
            json.dump(config_data, f, indent=4)
        print(f"Saved {len(machines)} virtual machine to config file")
        logger.info(f"Saved {len(machines)} virtual machines to instances.json")
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
                return config_data.get('machines', [])
        else:
            return []
    except Exception as e:
        print(f"Error loading configuration: {e}")
        logger.error(f"Failed to load config: {e}")
        return []

def provision_machines(machine_configs):
    # Function creates Machine objects & simulates provisioning
    provisioned_machines = []
    
    print("\n" + "="*50)
    print("Starting Infrastructure Provisioning...")
    print("="*50)
    
    for machine in machine_configs:
        print(f"\nProvisioning machine: {machine['name']}")
        print("-" * 30)
        if provision_machine(machine):
            provisioned_machines.append(machine)
            print(f"Successfully provisioned {machine['name']}")
        else:
            print(f"Failed to provision {machine['name']}")
    return provisioned_machines

def provision_machine(machine):
    # Simulate provisioning logic (was Machine.provision())
    # You can add more logic here as needed
    logger.info(f"Provisioning machine: {machine['name']}")
    # Simulate always successful
    return True
def install_services(machines):
    # This function pretends to install services on our machines
    print("\n" + "="*50)
    print("Starting Service Installation...")
    print("="*50)
    
    for machine in machines:
        print(f"\nInstalling services on machine: {machine['name']}")
        print("-" * 40)
        try:
            # Executes bash script to simulate Nginx installation
            import subprocess
            script_path = 'scripts/call_nginx.sh'
            if not os.path.exists(script_path):
                raise FileNotFoundError(f"Script {script_path} not found")
            print(f"Running installation script for {machine['name']}...")
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
            logger.info(f"Installation script ran successfully for {machine['name']}")
            print(f"Installation script ran successfully for {machine['name']}")
        except FileNotFoundError as e:
            error_msg = f"Installation script not found for {machine['name']}: {e}"
            print(error_msg)
            logger.error(error_msg)
        except subprocess.CalledProcessError as e:
            error_msg = f"Failed installation for {machine['name']}: {e}"
            print(error_msg)
            logger.error(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error installation for {machine['name']}: {e}"
            print(error_msg)
            logger.error(error_msg)

def show_menu():
    #Function tells user what actions they can take
    print("\n" + "="*50)
    print("DevOps Infrastructure Automation Program")
    print("="*50)
    print("1. Create new virtual machines")
    print("2. Show any existing machines")
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
        print(f"{i}. Name: {machine['name']}")
        print(f"   OS: {machine['os']}")
        print(f"   CPU: {machine['cpu']} cores")
        print(f"   RAM: {machine['ram']} GB")
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
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            # Create new machines
            print("\nCreating new virtual machines...")
            machines = get_user_input()
            if machines:
                if save_machines_to_config(machines):
                    print("Virtual Machines successfully created! Hooray!")
                else:
                    print("Error trying to save virtual machine...Boo!")
            else:
                print("No virtual machines created. Sadface...")
        
        elif choice == '2':
            # Show existing machines
            show_existing_machines()
        
        elif choice == '3':
            # Provision all machines
            machines = load_machines_from_config()
            if machines:
                provision_machines(machines)
            else:
                print("No virtual machines found. Please first create a virtual machine before continuing...")
        
        elif choice == '4':
            # Installation services
            machines = load_machines_from_config()
            if machines:
                install_services(machines)
            else:
                print("No virtual machines found. Please first create a virtual machine before continuing...")
        
        elif choice == '5':
            # Full automation
            print("\nStarting full automation process...")
            machines = get_user_input()
            if machines:
                # Saves vm's
                if save_machines_to_config(machines):
                    # Provisioning vm's
                    provisioned_machines = provision_machines(machines)
                    # Installation services
                    install_services(provisioned_machines)
                    print("\nAutomation successfully completed! Hooray!")
                else:
                    print("Automation Error!! Could not save virtual machine...Boo!")
            else:
                print("No virtual machines created. Automation cancelled.")
        
        elif choice == '6':
            # Exit
            print("Thank you for using my DevOps Infrastructure Automation Program!")
            logger.info("DevOps Automation Program stopped")
            break
        
        else:
            print("Invalid option. Please enter a number between 1 and 6.")
        
        # Wait for user to press Enter before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
