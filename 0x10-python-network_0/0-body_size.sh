#!/bin/bash
# Script that send request to that URL and displays the size of the body in byte
curl -s "$1" | wc -c
