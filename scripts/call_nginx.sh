#!/bin/bash

# Script simulates installation / configuration of Nginx
# Will not really install Nginx, only print messages as a simulation

echo "Starting Nginx installation process..."
echo "Checking system requirements..."

# Simulates checking whether correct user is running script
if [ "$EUID" -ne 0 ]; then
    echo "NOTE: For real world case, this needs admin privileges"
fi

# Simulates updating package lists
echo "Updating package lists"
sleep 1
echo "Package lists successfully updated! Hooray!"

# Simulates checking if Nginx is already installed
echo "Checking if Nginx is installed"
sleep 1
echo "Nginx is not installed...Continue to installation"

# Simulates Nginx installation
echo "Installing Nginx"
sleep 2
echo "Nginx successfully installed! Hooray!"

# Simulates starting / enabling Nginx
echo "Starting Nginx..."
sleep 1
echo "Nginx service has successfully started! Hooray!"

echo "Enabling Nginx to open on startup..."
sleep 1
echo "Nginx automation enabled! Hooray!"

# Simulates checking if Nginx is running
echo "Verify Nginx installation is running..."
sleep 1
echo "Nginx is running! Hooray!"

# Simulates firewall configuration
echo "Configuring firewalls for Nginx..."
sleep 1
echo "Firewalls configured! Hooray, your machine is secured!"

echo "Nginx installation & configuration successfully completed! Congratulations!!!"
echo "Server is now ready..."

# Writes to logfile that installation completed
echo "$(date): Nginx installation simulation complete" >> logs/nginx_install.log
