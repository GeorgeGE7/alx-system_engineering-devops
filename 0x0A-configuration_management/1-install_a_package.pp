#!/usr/bin/pup
# Install flask 2.1.0 by pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['pip'],
}
