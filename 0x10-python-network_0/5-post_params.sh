#!/bin/bash
# Script to POST to header email as test@gmail.com & subject as "I will always be here for PLD"
curl -s -d -X POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
