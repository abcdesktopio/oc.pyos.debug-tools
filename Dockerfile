
# Default release is 20.04
ARG BASE_IMAGE_RELEASE=22.04
# Default base image 
ARG BASE_IMAGE=ubuntu


# Start here
FROM $BASE_IMAGE:$BASE_IMAGE_RELEASE
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends  \
        curl                            \
        apt-transport-https             \
        ca-certificates                 \
        gnupg-agent                     \
        software-properties-common      \
	gnupg2 				\
    && apt-get clean                    \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends  \
	python3 		\
	python3-pip		\ 
	python3-distutils	\
	python3-kerberos	\
	python3-setuptools	\
	libglib2.0-0		\
    && apt-get clean            \
    && rm -rf /var/lib/apt/lists/*

COPY /hellokube.py / 
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - 
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list 

RUN apt-get update && apt-get install -y --no-install-recommends  \
	kubectl			\
    	telnet	  		\
    	wget			\
    	netcat			\
    	iputils-ping		\
    	dnsutils		\
	net-tools 		\
	vim			\
    && apt-get clean            \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install kubernetes

CMD ["/usr/bin/python3", "/hellokube.py"]
