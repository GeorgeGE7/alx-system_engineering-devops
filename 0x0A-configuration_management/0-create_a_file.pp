# Creating a file in /tmp called school

file { '/tmp/school':
  content => 'I love Puppet',
  mode => '0744',
  owner => 'www-data',
  group => 'www-data',
  }