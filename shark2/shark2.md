# Wireshark twoo twooo two twoo... Solution
(I needed help to get ideas about using subdomamins together to form a base 64 string)

First idea was to filter packets with `http`.

We can see that many `GET /flag` requests are made but there are too many responses with different flags. None of these are the real flag. 

These requests are made to `Destination Address: ec2-18-217-1-57.us-east-2.compute.amazonaws.com (18.217.1.57)`.  

DNS requests are made to a particular domain `reddshrimpandherring.com`.

By filtering with `dns && ip.addr == 18.217.1.57`, we get :

![[capture.png]]

To extract data i used `File > Export Packet Dissections > As Plain Text` to get `shark2_dns_domain.txt`.

Then to extract domain names in a separate file from these packets I did : 
```bash
grep "Name: " shark2_dns_domains.txt  | uniq > shark2_domain_names.txt
```

And then to concatenate the (apparently suspicious base64 looking subdomains) and decode from base 64 :
```bash
sed -n 's/.*Name: \([^\.]*\)\.reddshrimpandherring.*/\1/p' shark2_domain_names.txt  | uniq | tr -d '\n' | base64 -d
```

Which gives `picoCTF{dns_3xf1l_ftw_deadbeef}`.