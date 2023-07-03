#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me


##!/bin/bashi
## catch me if you can
#curl -s -X PUT 0.0.0.0:5000/catch_me -o /dev/null -w "%{redirect_url}"| xargs curl -sL -X PUT -H 'Origin:School' -F 'user_id= 98'
