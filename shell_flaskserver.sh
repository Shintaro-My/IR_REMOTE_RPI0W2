#!/bin/sh

cd /home/pi/IR_REMOTE_RPI0W2
for i in {1..5}
do
    sudo -H -u pi python3 flaskserver.py
    if [ $? -eq 0 ]; then
        echo "Success"
        break
    else
        sleep 5
    fi
done
if [ $i -eq 5 ]; then
    echo "Retry failed"
fi