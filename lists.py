from bs4 import BeautifulSoup
import sys

"""
Script to make lists from my exported chrome bookmarks.
"""
def url_label_pairs(soup):
  links = soup.find_all('a')
  return [(link['href'], link.text) for link in links]

filename = sys.argv[1]
soup = BeautifulSoup(open(filename))
remaining = soup.find_all('h3', text='Remaining Readings')[0].parent.dl
completed = soup.find_all('h3', text='Completed Readings')[0].parent.dl
remaining_urls_and_labels = url_label_pairs(remaining)
completed_urls_and_labels = url_label_pairs(completed)

books = ["Java Concurrency in Practice",
"ZooKeeper: Distributed Process Coordination (O'Reilly)",
"Head First Design Patterns",
"Linux System Programming 2nd Edition (O'Reilly)",
"TCP/IP Illustrated, Vol. 1: The Protocols",
"CONSENSUS: BRIDGING THEORY AND PRACTICE (Diego Ongaro's PhD raft dissertation)",
"The Rust Programming Language",
"Rust by Example",
"OASIS Advanced Message Queuing Protocol (AMQP) Version 1.0",
"C++ Concurrency in Action",
"Effective Modern C++"]

for pair in remaining_urls_and_labels:
  print("""<li><a href="%s">%s</a></li>""" % pair)

for book in books:
  print("<li>%s</li>" % book)

for pair in completed_urls_and_labels:
  print("""<li><a href="%s">%s</a></li>""" % pair)
