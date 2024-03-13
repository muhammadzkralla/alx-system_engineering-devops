# 0-the_sky_is_the_limit_not.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Update Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.html index.htm;

    server_name localhost;

    location / {
        try_files $uri $uri/ =404;
    }
}
',
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
