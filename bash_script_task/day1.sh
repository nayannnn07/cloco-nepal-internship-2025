#!/bin/bash

# -----------Task 1: Directory Management--------------

echo "----- Task 1: Directory Management -----"

# Create project_files directory in home
echo "Creating the directory named "project_files" in the /home directory"
mkdir /home/nayana/project_files
echo "The project_files directory has been created."
echo ""

# -----------Task 2: User and Group Management-------------

echo "----- Task 2: User and Group Management -----"

# Create developers group
echo "Creating the group named developers"
sudo groupadd developers
echo "The group developers has been created." 
echo ""

# Create new user
echo "Creating the new user named intern_user"
sudo useradd intern_user
echo "The new user intern_user has been created." 
echo ""

# Add new user to the group
echo "Adding the user named intern_user to the developers group"
sudo usermod -aG developers intern_user
echo "The new user intern_user has been added to developers group."
echo ""

# Set password for user
echo "Setting an appropriate password for the user"
sudo passwd intern_user
echo "The password has been set for the user"
echo ""

# -----------Task 3: Permissions and Ownership-------------

echo "----- Task 3: Permissions and Ownership -----"

#Change ownership of project_files
echo "Changing the ownership of the project_files directory to intern_user and group developers"
sudo chown intern_user:developers /home/nayana/project_files
echo "The ownership of project_files has been changed."
echo ""

# Set appropriate permissions
echo "Setting appropriate permissions to owners, groups and others"
sudo chmod 750 /home/nayana/project_files
echo "The permission has been set."
echo ""

# -----------Task 4: Additional Tasks--------------

echo "----- Task 4: Additional Tasks -----"

# Create a welcome text file inside the "project_files"
sudo touch /home/nayana/project_files/welcome.txt
echo "Welcome.txt file has been created."
echo ""

# Append content to the file
echo "Adding contents to welcome.txt file"
echo ""

# Write the creation date and time to welcome.txt
echo "Creation Date: $(date)" | sudo tee /home/nayana/project_files/welcome.txt

# Append the directory path to the file
echo "Directory Path: /home/nayana/project_files" | sudo tee -a /home/nayana/project_files/welcome.txt 

# Append the owner of the directory to the file
echo "Owner: $(stat -c '%U' /home/nayana/project_files)" | sudo tee -a /home/nayana/project_files/welcome.txt

# Append the group of the directory to the file
echo "Group: $(stat -c '%G' /home/nayana/project_files)" | sudo tee -a /home/nayana/project_files/welcome.txt 
echo "The content has been added to the file."
echo ""

# Set appropriate permissions for welcome.txt
echo "Setting appropriate permission for welcome.txt file"
sudo chmod 744 /home/nayana/project_files/welcome.txt
echo "The permission has been set for welcome.txt file."
echo ""

# -----------Task 5: Verification--------------

echo "----- Task 5: Verification -----"

# Verify directory creation and permissions
echo "Verifying directory creation and permissions:"
ls -ld /home/nayana/project_files
echo ""

# Verify user creation and group membership
echo "Verifying user creation and group membership:"
id intern_user
echo ""

# Verify file creation and contents 
echo "Verifying file creation and contents:"
sudo cat /home/nayana/project_files/welcome.txt
echo ""
