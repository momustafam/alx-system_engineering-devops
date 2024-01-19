# Install flask with 2.1.0 version
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
