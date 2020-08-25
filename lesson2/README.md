## 配置

部署拓扑图如下：

![](./deploy-topo.png)

集群部署在4台机器上面。tdib和pd一起部署在**node1**结点。tikv部署了三个结点，分别是**kv-node1**、**kv-node2**、**kv-node3**.

它们的配置如下：

| 结点     | 配置详情                                                     |
| -------- | ------------------------------------------------------------ |
| node1    | CPU：8核，内存：16 GiB，磁盘规格型号：200GiB (11800 IOPS)，单盘IOPS性能上限5万 |
| kv-node1 | CPU：8核，内存：32 GiB，磁盘规格型号：256GiB (14600 IOPS)，单盘IOPS性能上限5万 |
| kv-node2 | CPU：8核，内存：32 GiB，磁盘规格型号：256GiB (14600 IOPS)，单盘IOPS性能上限5万 |
| kv-node3 | CPU：8核，内存：32 GiB，磁盘规格型号：256GiB (14600 IOPS)，单盘IOPS性能上限5万 |

TiDB Dashboard中集群信息如下：

### 实例

![](./instance.png)

### 主机

![](./hosts.png)

### 服务配置

#### tidb

```
tidb:
    log.slow-threshold: 300
    binlog.enable: false
    binlog.ignore-error: false
    mem-quota-query: 5368709120
```

#### tikv

```
tikv:
    readpool.storage.use-unified-pool: false
    readpool.coprocessor.use-unified-pool: true
```

## 测试

### go-ycsb

#### workloada

##### 结果

![](go-ycsb/workloada/result.png)

##### 监控

tidb-qps

![](go-ycsb/workloada/monitor/tidb-summary-qps.png)

tidb-duration

![](go-ycsb/workloada/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-ycsb/workloada/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-ycsb/workloada/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-ycsb/workloada/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-ycsb/workloada/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-ycsb/workloada/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### workloadb

##### 结果

![](go-ycsb/workloadb/result.png)

##### 监控

tidb-qps

![](go-ycsb/workloadb/monitor/tidb-summary-qps.png)

tidb-duration

![](go-ycsb/workloadb/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-ycsb/workloadb/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-ycsb/workloadb/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-ycsb/workloadb/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-ycsb/workloadb/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-ycsb/workloadb/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### workloadc

##### 结果

![](go-ycsb/workloadc/result.png)

##### 监控

tidb-qps

![](go-ycsb/workloadc/monitor/tidb-summary-qps.png)

tidb-duration

![](go-ycsb/workloadc/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-ycsb/workloadc/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-ycsb/workloadc/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-ycsb/workloadc/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-ycsb/workloadc/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-ycsb/workloadc/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### workloadd

##### 结果

![](go-ycsb/workloadd/result.png)

##### 监控

tidb-qps

![](go-ycsb/workloadd/monitor/tidb-summary-qps.png)

tidb-duration

![](go-ycsb/workloadd/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-ycsb/workloadd/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-ycsb/workloadd/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-ycsb/workloadd/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-ycsb/workloadd/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-ycsb/workloadd/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### workloade

##### 结果

![](go-ycsb/workloade/result.png)

##### 监控

tidb-qps

![](go-ycsb/workloade/monitor/tidb-summary-qps.png)

tidb-duration

![](go-ycsb/workloade/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-ycsb/workloade/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-ycsb/workloade/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-ycsb/workloade/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-ycsb/workloade/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-ycsb/workloade/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### workloadf

##### 结果

![](go-ycsb/workloadf/result.png)

##### 监控

tidb-qps

![](go-ycsb/workloadf/monitor/tidb-summary-qps.png)

tidb-duration

![](go-ycsb/workloadf/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-ycsb/workloadf/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-ycsb/workloadf/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-ycsb/workloadf/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-ycsb/workloadf/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-ycsb/workloadf/monitor/tikv-grpc-avg-duration.png)

##### 分析

### sysbench

#### oltp_point_select

##### 结果

![](sysbench/oltp_point_select/result1.png)

##### 监控

tidb-qps

![](sysbench/oltp_point_select/monitor/tidb-summary-qps.png)

tidb-duration

![](sysbench/oltp_point_select/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](sysbench/oltp_point_select/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](sysbench/oltp_point_select/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](sysbench/oltp_point_select/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](sysbench/oltp_point_select/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](sysbench/oltp_point_select/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### oltp_read_only

##### 结果

![](sysbench/oltp_read_only/result.png)

##### 监控

tidb-qps

![](sysbench/oltp_read_only/monitor/tidb-summary-qps.png)

tidb-duration

![](sysbench/oltp_read_only/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](sysbench/oltp_read_only/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](sysbench/oltp_read_only/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](sysbench/oltp_read_only/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](sysbench/oltp_read_only/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](sysbench/oltp_read_only/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### oltp_update_index

##### 结果

![](sysbench/oltp_update_index/result.png)

##### 监控

tidb-qps

![](sysbench/oltp_update_index/monitor/tidb-summary-qps.png)

tidb-duration

![](sysbench/oltp_update_index/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](sysbench/oltp_update_index/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](sysbench/oltp_update_index/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](sysbench/oltp_update_index/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](sysbench/oltp_update_index/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](sysbench/oltp_update_index/monitor/tikv-grpc-avg-duration.png)

##### 分析

### go-tpc

#### tpc-c

##### 结果

![](go-tpc/tpc-c/result.png)

##### 监控

tidb-qps

![](go-tpc/tpc-c/monitor/tidb-summary-qps.png)

tidb-duration

![](go-tpc/tpc-c/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-tpc/tpc-c/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-tpc/tpc-c/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-tpc/tpc-c/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-tpc/tpc-c/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-tpc/tpc-c/monitor/tikv-grpc-avg-duration.png)

##### 分析

#### tpc-h

##### 结果

![](go-tpc/tpc-h/result.png)

##### 监控

tidb-qps

![](go-tpc/tpc-h/monitor/tidb-summary-qps.png)

tidb-duration

![](go-tpc/tpc-h/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![](go-tpc/tpc-h/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![](go-tpc/tpc-h/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![](go-tpc/tpc-h/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![](go-tpc/tpc-h/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![](go-tpc/tpc-h/monitor/tikv-grpc-avg-duration.png)

##### 分析