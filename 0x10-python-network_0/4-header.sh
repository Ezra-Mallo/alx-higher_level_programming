#!/bin/bash
# Script that sends GET request and set header variable X-School-User-Id = 98
curl -sH "X-School-User-Id=98" "$1"
