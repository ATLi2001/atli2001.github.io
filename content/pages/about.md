Title: About
Slug: index
URL: /
Save_as: index.html

<div class="profile float-left">
  <img
    src="/images/austin_li.jpg"
    class="img-fluid z-depth-1 rounded"
    alt="Profile photo"
  >
  <div class="more-info">
    <p>CS PhD at Cornell University</p>
    <p>atl63@cornell.edu</p>
  </div>
</div>

## About

I'm a Computer Science PhD student at Cornell University where I am advised by [Lorenzo Alvisi](https://www.cs.cornell.edu/lorenzo/).
I am broadly interested in distributed systems, cloud computing, and the challenges in creating efficient, durable, consistent, and fault tolerant systems.
I previously completed my Bachelor's and Master's in Computer Science at Princeton University, where I worked with [Amit Levy](https://www.amitlevy.com/) and [Wyatt Lloyd](https://www.cs.princeton.edu/~wlloyd/).
Outside research, I like to play soccer, pickleball, and read.
You can find a copy of my CV [here](/pdfs/AustinLiCV.pdf).

My current research focuses on revisiting correctness for Byzantine fault-tolerant  (BFT) transactional systems. 
Despite provding strong safety guarantees, the adoption of these systems has been hampered by issues with scalability and developer convenience. 
To address this, recent work has shifted to a client-centric BFT database architecture.
However, this creates a signicant vulnerability: Byzantine clients are now able to violate the integrity of the database.
We build a system, Sintr, that provides a general framework for restoring safety to client-centric BFT databases while retaining their benefits.
