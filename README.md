# devops-automation
DevOps Infrastructure Provisioning and Configuration Automation Project

# DevOps Infrastructure Automation Program Project

## Project Overview

This is a DevOps infrastructure provisioning & configuration automation project. The program simulates the process of creating a virtual machine and installing services. This is a project is an exercise that demonstrates:

- Python programming for use in DevOps
- Input validation & error handling
- Integration between Python & Bash scripts
- Logging & monitoring
- JSON configuration management
- Git Version Control

## What This Program Does


1. **Menu Style Interface**: Using QA experience, user experience added with menu-style interface & multiple operation options for friendly navigation
2. **Collects User Input**: Asks user to define virtual machine & name it, which OS to use for machine, CPU cores, and RAM GB specs
3. **Validation Input**: Ensures all user input is correct & secure using python Machine class & Pydantic validation, with error handling added from QA testing experience
4. **Complete Automation**: Option 1 provides full end-to-end workflow - creates, provisions, and installs services in one step
5. **Simulates Provisioning**: Simulates creation of virtual machines using Python class "Machine" (prints messages instead of actually creating VMs)
6. **Installs Services**: Executes Bash script which simulates installing Nginx on each machine
7. **Logging File**: Keeps track of all actions in log files


## Setup & Installation

### Prerequisites
- Python 3
- Git
- Bash Shell (macOS / Linux)
- Pydantic (Python library for data validation)

### Installation Steps
**Note:** All commands below should be run in a terminal (not Python / IDE).
1. Clone repository:
git clone https://github.com/shaked-sharon/devops-automation.git
cd devops-automation
2. Install required Python package:
pip install pydantic
3. Make Bash script executable:
chmod +x scripts/setup_nginx.sh
4. Run application:
python3 infra_simulator.py


## How to Use

1. **Start Application**:
python3 infra_simulator.py
2. **Choose from menu options**:
- **Option 1**: Create new virtual machine, provision it, & install services (Shows full workflow)
- **Option 2**: View any virtual machines already created
- **Option 3**: Simulate provisioning existing virtual machines only
- **Option 4**: Simulate installation services on existing virtual machines only
- **Option 5**: Full automation (same as Option 1 - Create, provision, install)
- **Option 6**: Exit program
3. **Follow prompts** to enter virtual machine details:
- **Machine name**: Name your machine!
- **Operating system**: Choose OS--i.e. - Ubuntu, CentOS, Windows, MacOS
- **CPU**: Enter a number in given range
- **RAM**: Enter a number in given range in GB


## Files Explained

- **infra_simulator.py**: Main program runs everything. Machines are represented as Python classes (`Machine`); all provisioning & installation logic is handled by class methods & function
- **src/machine.py**: Contains the `Machine` class, which uses Pydantic for input validation & provides methods for provisioning & data
- **src/logger.py**: Writes messages to log file--keeps track of program
- **scripts/setup_nginx.sh**: Simulates Nginx installation without actually installing it
- **configs/instances.json**: Stores info about virtual machine created
- **logs/**: Folder contains log files that tracks & logs what program does

## Education Goals

This project teaches:
- Basic Python programming concepts
- How to use classes & Pydantic
- File handling & JSON processing
- Input validation & error handling
- Integration between Python & Bash
- Logging & monitoring--best practices
- Git version control

## Future Additions

This project is designed to be updated with the DevOps course. The project is meant for upgrading versions such as:
- Integration of cloud services (i.e. - AWS)
- Actual infrastructure provisioning using Terraform
- Database integrations for storing configurations
- Additional complex service installations
- Monitoring & alerting options

## Author

Sharon Shaked (shaked-sharon)
Email: sharon.shaked@icloud.com / sharon.shaked24@gmail.com

## License

This project is for educational purposes only



