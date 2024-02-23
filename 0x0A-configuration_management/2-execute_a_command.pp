# Kill process named killmenow by pkill

exec { 'pkill':
  command => 'pkill killmenow'
}
