#!/bin/bash
Recipient="admin@example.com"
Subject="Greeting"
Message="Welcome to our site"
mail -s $subject $Recipient <<< $Message
