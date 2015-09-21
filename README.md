# ugitstat

This is a very simple git repo status server. I use it every time I need to deploy fresh code into a remote machine.

To simplify: one of my servers is running in a private network enviroment and there is no chance even to pierce a tiny hole in the NAT. To workaround that I have built a dummy UDP server: it which shows current state of a git repo and polls that server from the NATed machine.

Check-out .ugitstat file for more details.
