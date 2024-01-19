# Kills a process named `killmeknow`
exec {'killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
