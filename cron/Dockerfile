FROM ubuntu:latest

RUN apt-get update && apt-get -y install cron curl

# Copy hello-cron file to the cron.d directory
COPY requestAPI /etc/cron.d/requestAPI
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/requestAPI

# Apply cron job
RUN crontab /etc/cron.d/requestAPI
 
# Run the command on container startup
CMD ["cron", "-f"]
