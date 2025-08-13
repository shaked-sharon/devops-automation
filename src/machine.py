# Uses Pydantic for data validation inherited from BaseModel
# Uses schema for simulation > virtual machines
# Each virtual machine will have unique name by user, OS, cpu core, & ram GB

from pydantic import BaseModel, field_validator

ALLOWED_OSES = {"ubuntu", "centos", "windows", "macos"}

class Machine(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int

    @field_validator('name')
    def validate_name(cls, v):
        if not v or not v.strip():
            raise ValueError("Machine name cannot be empty.")
        return v

    @field_validator('os')
    def validate_os(cls, v):
        if v.lower() not in ALLOWED_OSES:
            raise ValueError(f"Invalid OS: {v}. Allowed values are: Ubuntu, CentOS, Windows, MacOS.")
        return v

    @field_validator('cpu')
    def validate_cpu(cls, v):
        if not (2 <= v <= 64):
            raise ValueError("CPU cores must be between 2 and 64.")
        return v

    @field_validator('ram')
    def validate_ram(cls, v):
        if not (1 <= v <= 128):
            raise ValueError("RAM must be between 1 and 128 GB.")
        return v

    def to_dict(self):
        return self.model_dump()

    def provision(self):
        print(f"Creating virtual machine: {self.name}")
        print(f"Operating System: {self.os}")
        print(f"CPU: {self.cpu} cores")
        print(f"RAM: {self.ram} GB")
        print(f"Virtual Machine {self.name} has successfully been created! Hooray!")
        # Use the main logger instead of separate logging
        from src.logger import logger
        logger.info(f"Provisioned virtual machine: {self.name} - {self.os}, {self.cpu} CPU, {self.ram} GB RAM")
        return True
