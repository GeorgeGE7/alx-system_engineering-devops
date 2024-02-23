#!/usr/bin/env bash
# Modify ssh conf with Puppet

file { '/etc/ssh/ssh_config':
  ensure => present
}

file_line { 'Make password auth no':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true
}

file_line { 'Identity file path':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
