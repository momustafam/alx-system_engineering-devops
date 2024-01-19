# Kills a process named `killmeknow`
exec {'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}
