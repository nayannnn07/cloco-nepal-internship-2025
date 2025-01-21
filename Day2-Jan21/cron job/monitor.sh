#!/bin/bash

#Lists the top 5 processes using the most system resources
echo "Listing the top 5 processes" >> /home/nayana/Desktop/intern/Day2-Jan21/cron job/monitor.log
echo "" >> /home/nayana/Desktop/intern/Day2-Jan21/cron job/monitor.log

ps -eo pid,ppid,%cpu,%mem --sort=-%cpu |  head -n 6 >> /home/nayana/Desktop/intern/Day2-Jan21/cron job/monitor.log

echo "Timestamp of Log File" >> /home/nayana/Desktop/intern/Day2-Jan21/cron job/monitor.log
echo ""

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
echo "Log file created on $TIMESTAMP" >> /home/nayana/Desktop/intern/Day2-Jan21/cron job/monitor.log
echo "------------------------------------" >> /home/nayana/Desktop/intern/Day2-Jan21/cron job/monitor.log

