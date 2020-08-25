#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : zenk
# 2020-08-25 18:31

import os


tmplCase = '''
### {caseName}'''

tmplSubCase = '''
#### {subCaseName}

##### 结果

![]({caseName}/{subCaseName}/result.png)

##### 监控

tidb-qps

![]({caseName}/{subCaseName}/monitor/tidb-summary-qps.png)

tidb-duration

![]({caseName}/{subCaseName}/monitor/tidb-summary-duration.png)

tikv-cluster-qps

![]({caseName}/{subCaseName}/monitor/tikv-cluster-qps.png)

tikv-cluster-CPU

![]({caseName}/{subCaseName}/monitor/tikv-cluster-cpu.png)

tikv-grpc-qps

![]({caseName}/{subCaseName}/monitor/tikv-grpc-qps.png)

tikv-grpc-duration

![]({caseName}/{subCaseName}/monitor/tikv-grpc-duration.png)

tikv-grpc-avg-duration

![]({caseName}/{subCaseName}/monitor/tikv-grpc-avg-duration.png)'''

cases = list(dict(caseName=root[2:], subCaseName=dirs) for root, dirs, _ in os.walk('.')
             if root.startswith('./') and root.rfind('/') == 1)

for c in cases:
    print(tmplCase.format(**c))
    for cs in sorted(c['subCaseName']):
        # print(cs)
        print(tmplSubCase.format(caseName=c['caseName'], subCaseName=cs))
