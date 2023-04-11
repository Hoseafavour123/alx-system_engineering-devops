#Set up Client Configuration file in puppet

exec {'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
       path => '/bin/'
}
