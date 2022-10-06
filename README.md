# crontab

Instructions for automating the python file using crontab:

1. Pull down data from API into a python file

2. Create a new virtual machine 

3. git clone the crontab repo

4. cd into python file

5. Open the crontab file using crontab -e and add in the cron job command with path:

Once a day at 1pm:

0 1 * * *

Every Sunday night at 10:00pm: 

0 22 * * SUN

Pull down data at the end of every quarter:  

0 0 1 */3 *

6. status check: systemctl status cron

7. Save the retrieved data to the local machine where cron job is running
