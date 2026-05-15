FROM ubuntu:18.04
LABEL maintainer="contact@deehub.com"
RUN apt-get -y update && apt-get -y install nginx
COPY default /etc/nginx/sites-available/default
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]