# configure ssh configuration using puppet
file_line {'Turn off pas auth':
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no'
}

file_line {'Turn on auth with pk':
	path => '/etc/ssh/ssh_config',
	line => 'IdentityFile ~/.ssh/school'
}
