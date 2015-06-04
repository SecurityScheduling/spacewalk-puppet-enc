# Spacewalk as a Puppet ENC

This script is used to demonstrate how to use
Spacewalk (http://spacewalk.redhat.com/) as a
Puppet External Node Classifier.

1. Download the script to /usr/bin
2. Configure your puppet master to use the script

```
[main]
...
node_terminus = exec
    external_nodes = /usr/bin/spacewalk-enc.py
```
3. Add a Custom System Info key named puppet_role
4. In the System Details -> Custom Info edit the value
to represent the role you want to assign.

i.e.: roles::webserver
5. Enjoy

