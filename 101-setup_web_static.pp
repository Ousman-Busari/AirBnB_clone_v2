# script that sets web servers for the deployment of web_static

$conf_settings = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By 87373-web-01;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
    	alias /data/web_static/current;
	index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package {'nginx':
    ensure   => present,
    provider => 'apt',
}

-> file {'/data':
    ensure => directory,
}

-> file {'/data/web_static':
    ensure => directory,
}

-> file {'/data/web_static/releases':
    ensure => directory,
}

-> file {'/data/web_static/releases/test':
    ensure => directory,
}

-> file {'/data/web_static/shared':
    ensure => directory,
}

-> exec {'echo "Simple content to test Nginx configuration" > /data/web_static/releases/test/index.html':
    provider => shell,
}

-> exec {'ln -sf /data/web_static/releases/test/ /data/web_static/current':
    provider => shell,
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

-> file {'/etc/nginx/sites-available/default':
    ensure  => file,
    content => $conf_settings,
}

-> exec {'nginx restart':
    path => '/etc/init.d/',
}