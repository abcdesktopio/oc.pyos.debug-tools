# oc.pyos.debug-tools
simple debug tools for kubernetes troubleshooting with pyos
Contains a simple python script to check config and list pods in `$POD_NAMESPSACE`

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
kubectl apply -f pyos-debug-tools.yaml 
```

# to logs 

```
kubectl logs pyos-debug-tools -n abcdesktop
```
