#!/bin/bash
# set -x
job_name=$1
start_time=$2 # 2020-12-10T13:50:00.000+08:00
end_time=$3 # 2020-12-10T13:55:00.000+08:00


for pod_name in `curl -gs 'http://10.11.0.130:30900/api/v1/series?' --data-urlencode "match[]=kube_pod_labels{label_tf_job_name='${job_name}'}"  | jq -r  '.data[]|.pod'`
do
    # cpu usage
    curl -gs 'http://10.11.0.130:30900/api/v1/query_range?' --data-urlencode "start=${start_time}" --data-urlencode "end=${end_time}" --data-urlencode 'step=60' --data-urlencode "query=sum by (container_name) (rate(container_cpu_usage_seconds_total{container_name!='POD',pod_name='${pod_name}', container_name!=''}[75s]))" | jq .
    # cpu request
    curl -gs 'http://10.11.0.130:30900/api/v1/query_range?' --data-urlencode "start=${start_time}" --data-urlencode "end=${end_time}" --data-urlencode 'step=60' --data-urlencode "query=kube_pod_container_resource_requests_cpu_cores{pod='${pod_name}'}" | jq . 

    # mem usage
    curl -gs 'http://10.11.0.130:30900/api/v1/query_range?' --data-urlencode "start=${start_time}" --data-urlencode "end=${end_time}" --data-urlencode 'step=60' --data-urlencode "query=sum by (container_name) (container_memory_rss{pod_name='${pod_name}',container_name!='',container_name!='POD'})" | jq .

    # mem request
    curl -gs 'http://10.11.0.130:30900/api/v1/query_range?' --data-urlencode "start=${start_time}" --data-urlencode "end=${end_time}" --data-urlencode 'step=60' --data-urlencode "query=kube_pod_container_resource_requests_memory_bytes{pod='${pod_name}'}" | jq .

    # net recv
    curl -gs 'http://10.11.0.130:30900/api/v1/query_range?' --data-urlencode "start=${start_time}" --data-urlencode "end=${end_time}" --data-urlencode 'step=60' --data-urlencode "query=sort_desc(sum by (pod_name) (rate(container_network_receive_bytes_total{pod_name='${pod_name}'}[75s])))" | jq .

    # net trans
    curl -gs 'http://10.11.0.130:30900/api/v1/query_range?' --data-urlencode "start=${start_time}" --data-urlencode "end=${end_time}" --data-urlencode 'step=60' --data-urlencode "query=sort_desc(sum by (pod_name) (rate(container_network_transmit_bytes_total{pod_name='${pod_name}'}[75s])))" | jq . 

done