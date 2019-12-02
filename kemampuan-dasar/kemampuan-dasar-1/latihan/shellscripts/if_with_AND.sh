#! /bin/bash

echo "Enter username"
read username
echo "Enter password"
read password
if [[ ( $username == "admin" && $password == "secret" ) ]]; then
echo "Valid user"
else
echo "Invalid user"
fi
