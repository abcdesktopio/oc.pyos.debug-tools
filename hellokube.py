from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint
import os
import time

def main():
        # the config will be loaded from default location.
        print ("Initializing ...")
        time_to_sleep_in_second = 30
        try:   
            print( f"KUBERNETES_SERVICE_HOST={os.getenv('KUBERNETES_SERVICE_HOST')}" )
            print( f"KUBERNETES_SERVICE_PORT={os.getenv('KUBERNETES_SERVICE_PORT')}" ) 
            print( f"KUBERNETES_SERVICE_PORT_HTTPS={os.getenv('KUBERNETES_SERVICE_PORT_HTTPS')}" )
            config.load_incluster_config() # set up the client from within a k8s pod
            print( "load_incluster_config done" )
        except Exception as e_in:
            print(f"ODOrchestratorKubernetes load_kube_config" )
            print(f"use KUBE_CONFIG_DEFAULT_LOCATION = {os.environ.get('KUBECONFIG', '~/.kube/config')}")
            print( "ODOrchestratorKubernetes load_kube_config" )
            try:
                config.load_kube_config()
                print( f"load_kube_config done" )
            except Exception as e_out:
                print( f"This is a fatal error" )
                print( f"load_incluster_config failed {e_in}" )
                print( f"load_kube_config failed {e_out}" )
        v1 = client.CoreV1Api()
        namespace = os.environ.get('POD_NAMESPACE', 'abcdesktop')
        print( f"use namespace={namespace}" ) 
        print( f"listing pods in {namespace}:")
        while(True):
          try:
            api_response = v1.list_namespaced_pod(namespace=namespace, pretty=True)
            pprint(api_response)
          except ApiException as e:
            print("Exception when calling CoreV1Api->list_namespaced_pod: %s\n" % e)
          print( f"sleeping for {time_to_sleep_in_second}" )
          time.sleep(time_to_sleep_in_second)
if __name__ == '__main__':
    main()
