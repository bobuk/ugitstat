# ugitstat

Very simple git repo status server. I use it to deploy a fresh code into very remote server.
To simplify the explanation: one of my servers installed in very private network so there's no chance to pierce a hole in their NAT.
So I build a really dummy UDP server who shows a current state of git repo and poll this server from NAT'ed machine.

Check out .ugitstat file to understand anything else.
