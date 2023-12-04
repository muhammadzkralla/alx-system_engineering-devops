# Automating the nginx installing process and adding custom header.

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

exec { 'allow_http':
  command => 'ufw allow "Nginx HTTP"',
  path    => ['/bin', '/usr/bin'],
  unless  => 'ufw status | grep "Nginx HTTP"',
  require => Package['nginx'],
}
