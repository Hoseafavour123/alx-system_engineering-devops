# Install and configur nginx web server

#Update Packges
exec {"Update packages":
    command => "apt-get update",
    path    => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}

#Install nginx web server
package {"nginx":
    ensure => "installed",
}

#Allow HTTP for nginx
exec {"Allow HTTP":
    command => "ufw allow 'NGINX HTTP'",
    path    => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}

#Change rights to www file
exec {"Change owner":
    command => "chmod -R 755 /var/www",
    path    => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}

#Add index file
file {"Index file":
    path    => "/var/www/html/index.html",
    content => "Hello World!",
}

#Add error file
file {"Error File":
    path    => "/var/www/htm/custom404.html",
    content => "Ceci n'est pas une page",
}

#Add redirection and error page
file {"/etc/nginx/sites-enabled/default":
    ensure => file,
    content =>
        "server {
            listen 80 default_server;
            listen [::]:80 default_server;
            root /var/www/html;
            index index.html index.htm index.nginx-debian.html;
            server_name _;
            location / {
                    #first attempt to serve content as a file, then as directory
                    #and finallly fall to 404
                try_files \$uri \$uri/ custom404;
            }

            error_page 404 /custom404.html;
            location /custom404.html {
                internal;
            }
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }",
}

#Restart nginx
exec {"Restart service":
    command => "service nginx restart",
    path    => "/usr/bin:/usr/sbin:/bin",
}

#Start nginx service
service {"nginx":
    ensure  => running,
    require => Package['nginx'],
}

