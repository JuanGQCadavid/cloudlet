sudo service docker restart  \
&& sudo docker swarm leave --force  \
&& sudo docker stop $(sudo docker ps -a -q)  \
&& sudo docker system prune -f 