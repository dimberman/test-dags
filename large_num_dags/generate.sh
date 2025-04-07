#!/bin/bash
for i in {1..100}; do
    sed "s/<<template_num>>/$i/g" scale_dag.template > "scale_dag_file_${i}.py"
done