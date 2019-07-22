all_workers=(tolstoi lowe)
host=${all_workers[@]:0:1}
slaves=${all_workers[@]:1}
ray_path=/home/gestrela/signetms_env/bin/ray

ray_out=$(ssh $host $ray_path start --head 2>&1 >/dev/null)
echo "$ray_out"
redis_server_line=$(echo $ray_out | grep -oP '\s+ray start --redis-address \d+\.\d+\.\d+\.\d+:\d+')
redis_server_ip=$(echo $redis_server_line | grep -oP '\d+\.\d+\.\d+\.\d+:\d+')
echo "Starting redis server with ip: $redis_server_ip"

for worker in $slaves
do
    ray_out=$(ssh $worker $ray_path start --redis-address=$redis_server_ip)
    echo "Started ray on $worker"
done
