# Fix a problem of high requests proplem

exec {'replaceing':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restarting':
  provider => shell,
  command  => 'sudo service nginx restart',
}
