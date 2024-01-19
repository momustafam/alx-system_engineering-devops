# Kills a process named `killmeknow`
exec {'killmenow_process':
  command  => 'pkill killmenow',
  path     => 'usr/bin'
}
