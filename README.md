# ugitstat

This is a very simple git repo status server.

**Problem & Solution:**
Quite often I need to deploy fresh code into a remote machine running in a private network enviroment and there is no chance to pierce even a tiny hole in the NAT to get trough. To workaround that I have built a dummy UDP server: it shows current state of a git repo and polls that server from the NATed machine.

*Please refer to .ugitstat file for more details.*
