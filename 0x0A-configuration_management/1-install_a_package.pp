#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package { 'pip':
  ensure   => 'present',
  provider => 'pip',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['pip'],
}
