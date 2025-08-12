# devops-automation
DevOps Infrastructure Provisioning and Configuration Automation Project

# DevOps Infrastructure Automation Tool

## Project Overview

This is a DevOps infrastructure provisioning & configuration automation project. The program simulates the process of creating a virtual machine and installing services on it. This is a project exercise that demonstrates:

- Python programming for use in DevOps
- Input validation & error handling
- Integration between Python & Bash scripts
- Logging & monitoring
- JSON configuration management
- Git Version Control

## What This Tool Does


1. **Collects User Input**: Asks user to define a virtual machine with a name, the operating system, CPU, and RAM specifications
2. **Validation Input**: Ensures all user input is correct and secure using the Machine class and Pydantic validation
3. **Simulates Provisioning**: Simulates the creation of a virtual machine using a Python class (prints messages instead of actually creating VMs) -- no actual installation
4. **Installs Services**: Executes a Bash script that simulates installing Nginx
5. **Logging File**: Keeps track of all actions in log files


## Setup and Installation

### Prerequisites
- Python 3
- Git
- Bash Shell (macOS / Linux)

### Installation Steps
1. Clone this repository:
git clone https://github.com/shaked-sharon/devops-automation.git
cd devops-automation
2. Make the Bash script executable:
chmod +x scripts/call_nginx.sh
3. Run application:
python3 infra_simulator.py


## How to Use

1. **Start Application**:
python3 infra_simulator.py
2. **Choose from menu options**:
- **Option 1**: Create new virtual machine by entering specs
- **Option 2**: View any virtual machines already created
- **Option 3**: Simulate provisioning virtual machine
- **Option 4**: Simulate installation services of virtual machine
- **Option 5**: Automate the entire process
- **Option 6**: Exit program

3. **Follow prompts** to enter virtual machine details:
- **Machine name**: Name your machine!
- **Operating system**: Choose the OS--i.e. - CentOS, Windows
- **CPU**: Enter a number only
- **RAM**: Enter a number only in GB (i.e. 4 or 8)


## Files Explained

- **infra_simulator.py**: Main program that runs everything. Machines are represented as Python classes (`Machine`), and all provisioning and installation logic is handled by class methods and functions.
- **src/machine.py**: Contains the `Machine` class, which uses Pydantic for input validation and provides methods for provisioning and serialization.
- **src/logger.py**: Writes messages to log files
- **scripts/call_nginx.sh**: Simulates Nginx installation without actually installing it
- **configs/instances.json**: Stores info about virtual machine created
- **logs/**: Folder contains log files that tracks and logs what program does

## Education Goals

This project teaches:
- Basic Python programming concepts
- How to use classes and Pydantic for data and logic management
- File handling & JSON processing
- Input validation & error handling
- Integration between Python & Bash
- Logging & monitoring--best practices
- Git version control

## Future Enhancements

This project is designed to evolve. Future versions could include:
- Integration with cloud providers (AWS, Azure)
- Real infrastructure provisioning using Terraform
- Web interface for easier use
- Database integration for storing configurations
- More complex service installations
- Monitoring and alerting capabilities

## Author

Sharon Shaked (shaked-sharon)
Email: sharon.shaked@icloud.com

## License

This project is for educational purposes



