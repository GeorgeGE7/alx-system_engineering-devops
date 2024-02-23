# Kill process named killmenow by pkill

exec { 'killmenow':
  command => 'pkill killmenow',
}
