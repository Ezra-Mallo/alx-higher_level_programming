#!/bin/bash
# Script to POST to header email as test@gmail.com & subject as "I will always be here for PLD"
curl -s POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
