# kubeflow本地环境搭建

## 创建本地cluster环境

```shell
brew install kind

kind create cluster --config kind.yaml --image=kindest/node:v1.14.10
```

## 安装kubeflow pipeline

```shell
# env/platform-agnostic-pns hasn't been publically released, so you will install it from master
export PIPELINE_VERSION=1.3.0
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"

# verify  pipeline ui
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80

```

## 卸载kubeflow pipeline

```shell
export PIPELINE_VERSION=1.3.0
kubectl delete -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
kubectl delete -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
```

## 安装tf-operator

```shell
kubectl apply -f https://raw.githubusercontent.com/kubeflow/tf-operator/master/deploy/v1/tf-operator.yaml

```