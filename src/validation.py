# This file will chick if user enters good info / input
# Note to self: This should validate whether the input is correct

def validate_machine_input(name, os, cpu, ram):
    # List of problems we find
    errors = []
    
    # This checks that the name is not empty or too lengthy
    # If its too long > add error message to list (?)
    if not name or name.strip() == "":
        errors.append("Machine name cannot be empty")
    elif len(name) > 50:
        errors.append("Machine name is too long")
    
    # This checks if os = valid
    valid_os = ["ubuntu", "centos", "windows", "macos"]
    if not os or os.lower() not in valid_os:
        errors.append(f"Operating system must be one of: {', '.join(valid_os)}")
    
    # This checks if CPU has valid number
    try:
        cpu_num = int(cpu)
        if cpu_num < 1 or cpu_num > 32:
            errors.append("CPU must be a number between 1 and 32")
    except:
        errors.append("CPU must be a whole number (i.e. 2 or 4)")
    
    # This will check if RAM has valid number
    try:
        ram_num = int(ram)
        if ram_num < 1 or ram_num > 128:
            errors.append("RAM must be a number between 1 and 128 GB")
    except:
        errors.append("RAM must be a whole number (i.e. 4 or 8)")
    
    # This will "Return True" if no errors or "False" if > errors
    return len(errors) == 0, errors

def get_user_input():
    # Function asks user for machine input
    machines = []
    
    print("Welcome to my DevOps Automation Program!")
    print("Lets create a virtual machine! Very exciting!")
    print()
    
    while True:
        print("Enter the name of the virtual machine and follow the prompts (or type 'done' if youre finished):")
        
        # Gets name of  virtual machine
        name = input("Machine Name: ").strip()
        if name.lower() == 'done':
            break
        
        # Gets OS
        print("Available operating systems: Ubuntu, CentOS, Windows, MacOS")
        os = input("Operating system: ").strip()
        
        # Gets CPU (only number)
        cpu = input("CPU cores (2 - 64 cores): ").strip()
        
        # Gets RAM (only number)
        ram = input("RAM in GB (1 - 128): ").strip()
        
        # Checks if input is valid
        is_valid, error_messages = validate_machine_input(name, os, cpu, ram)
        
        if is_valid:
            # Adds vm to list
            machine_data = {
                "name": name,
                "os": os.lower(),
                "cpu": int(cpu),
                "ram": int(ram)
            }
            machines.append(machine_data)
            print(f"Machine '{name}' successfully added! Hooray!")
            print()
        else:
            # Shows user if something is wrong or if theres an issue
            print("There is a problem with your input:")
            for error in error_messages:
                print(f"- {error}")
            print("Please try again")
            print()
    
    return machines
