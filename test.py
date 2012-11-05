# coding=utf-8

import sys
from pyWebCrawler import Fetcher, Crawler
from tools import *
from graph import Generate_Graph, Display_Graph

# Global variable containing all the URLS following this scheme of node
# { "http_url", {"toCrawl" : bool, "parent" : "http_parent"} }
urls = dict()
# Global variable containing the final tree of all the urls following this scheme
# { "parent" : { "child1" : {}, "child2" : { "subchild1" : {} } }
tree = dict()

#######################################################################
# Starting point of the crawler : ask the user what he wants to crawl
http = raw_input("What webpage do you want to crawl [http(s) page]? ")
ending = raw_input("What is the ending condition [str]? ")
deep = raw_input("How deeper [int] do you want to go (None = infinite)? ")

# Verifying datas
if deep == "":
    deep = None
if ending == "":
    ending = None
if not (http.startswith("http") or http.startswith("https")):
    print "Invalid webpage"
    sys.exit(42)
try:
    deep = int(deep)
except:
    if deep != None:
        print "Invalid deep"
        sys.exit(42)

### CHEATING ENTRIES 
#http="http://etud.insa-toulouse.fr/~club_robot/forum/"
#ending="club_robot"
#deep=None
   
# Starts the crawler    
c = Crawler(http, urls, ending, deep)
c.crawl()
             
# Creates the tree structure using the URLS found previously
urls_to_tree(http, urls, tree)

# To debug : prints the tree at the end and the number of urls found
print "\n======= Finished, displaying the tree ========="
for i in tree.items():
    print i     
print "\n======= Number of urls found : ", len(urls), " ========"

### GRAPH PART ###
print "\n======= Generating the graph ========"
graph = Generate_Graph(http, urls, tree).graph
print "======= Displaying the graph ========"
Display_Graph(http, graph)