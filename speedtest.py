import speedtest

s = speedtest.Speedtest()
print("Download speed: ", s.download()/pow(10,6), " Mbps")
print("Upload speed: ", s.upload()/pow(10,6), " Mbps")

servernames = []
s.get_servers(servernames)
print("Ping: ", s.results.ping)
