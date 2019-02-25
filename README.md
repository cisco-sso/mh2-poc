# mh2-poc

Proof of Concept, Pure Python approach to Kubernetes Configuration Management

## Notes

https://pulumi.io/reference/python.html


# Convert
dave@kdk:~/Dev/framework-deploy/clusters/kube1.davidwang.com$ # cat mh/main.yaml |grep alias |grep -v '#'| awk '{print "mh simulate -p " $2 " | sponge | sed -n \"/Created tunnel using local port/q;p\" > " $2 ".yaml" }'
