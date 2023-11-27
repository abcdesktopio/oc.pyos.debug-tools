# oc.pyos.debug-tools
simple debug tools for kubernetes troubleshooting with pyos.

It contains a simple python script to check config and list pods in `$POD_NAMESPSACE`

Load the `load_incluster_config()` or `load_kube_config()`
```
try:
    config.load_incluster_config() # set up the client from within a k8s pod
except Exception as e_in:
    try:
        config.load_kube_config()
    except Exception as e_out:
        print( f"This is a fatal error" )
```

List pods in `$POD_NAMESPSACE`

```
time_to_sleep_in_second = 30
while(True):
  try:
    api_response = v1.list_namespaced_pod(namespace=namespace, pretty=True)
    pprint(api_response)
  except ApiException as e:
    print("Exception when calling CoreV1Api->list_namespaced_pod: %s\n" % e)
  print( f"sleeping for {time_to_sleep_in_second}" )
  sleep(time_to_sleep_in_second)
```

# To build

```
git clone https://github.com/abcdesktopio/oc.pyos.debug-tools.git
docker build -t abcdesktopio/pyos-debug-tools:main .
```

# To run 

```
kubectl apply -f https://raw.githubusercontent.com/abcdesktopio/oc.pyos.debug-tools/main/pyos-debug-tools.yaml
```

# To logs 

```
kubectl logs pyos-debug-tools -n abcdesktop
```

You should read on stdout

```
Initializing ...
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
load_incluster_config done
use namespace=abcdesktop
listing pods in abcdesktop:
{'api_version': 'v1',
 'items': [{'api_version': None,
            'kind': None,
            'metadata': {'annotations': None,
                         'creation_timestamp': datetime.datetime(2023, 10, 24, 14, 25, 7, tzinfo=tzlocal()),
                         'deletion_grace_period_seconds': None,
                         'deletion_timestamp': None,
                         'finalizers': None,
                         'generate_name': 'daemonset-nginx-',
                         'generation': None,
                         'labels': {'controller-revision-hash': '56984c456d',
                                    'name': 'daemonset-nginxpods',
                                    'netpol/dns': 'true',
                                    'netpol/memcached': 'true',
                                    'netpol/ocuser': 'true',
                                    'netpol/pyos': 'true',
                                    'netpol/speedtest': 'true',
                                    'pod-template-generation': '4',
                                    'run': 'nginx-od',
                                    'type': 'frontend,
                                    ...
[CUT HERE] 
```
