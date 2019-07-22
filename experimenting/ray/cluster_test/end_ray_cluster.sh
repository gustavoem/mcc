ray_path=/home/gestrela/signetms_env/bin/ray

readarray -t all_workers < servers_list.txt
for worker in "${all_workers[@]}"
do
    ssh $worker $ray_path stop
    echo "ending $worker"
done
