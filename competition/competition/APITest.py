import clearbit

clearbit.key = 'sk_8f708ad4e5975cdd82d69c0ba095c091'

people = clearbit.Prospector.search(domain='www.snapchat.com', role='marketing')




for person in people:
  print person['name']['fullName']
  print person['title']
  print 'Role: ' + person['role']
  print person['email']