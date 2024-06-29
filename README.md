# pyspark-docker
Pyspark en Docker Compose
##Para crear el swarm y conectar los pcs
#PC Nodo Maestro
docker swarm init –advertise-addr 192.168.20.32

#PC Nodo Trabajador
docker swarm join --token SWMTKN-1-3bw8u9ckc8imvah3tezr1nugn8mag8h49g9n54c34y728ljezc-b103e2pr2bf6mlur00cjrd5yp 192.168.20.32:2377

#PC Nodo Maestro

#Para ver los nodos conectados al swarm
docker node ls

docker compose up -d
##Navegamos a localhost:9090 para ver pyspark corriendo

#Para saber el nombre del contenedor
docker compose ps

#Enviamos los archivos necesarios para ejecutar la tarea al nodo spark-master
sudo docker cp ./jars/postgresql-42.2.2.jar proyectoinfraestructuras-spark-master-1:/opt/spark/jars

#Ejecutamos la tarea
sudo docker compose exec spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 
--jars /opt/spark/jars/postgresql-42.2.22.jar --driver-memory 1G --executor-memory 1G /opt/spark-apps/main.py


#Enviamos los archivos necesarios para ejecutar la tarea
sudo docker cp ./apps/wordcount.py proyectoinfraestructuras-spark-master-1:/opt/spark-apps
sudo docker cp ./apps/lorem-ipsum.txt proyectoinfraestructuras-spark-master-1:/opt/spark-apps

#Ejecutamos la tarea
sudo docker compose exec spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 --driver-memory 1G --executor-memory 1G /opt/spark-apps/wordcount.py

#Volvemos al navegador y vemos las tareas ejecutadas

##Para probar kafka

#Crear el topic
docker compose exec kafka kafka-topics --create --topic test-topic --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
#Producir mensajes
docker compose exec kafka kafka-console-producer --topic test-topic --bootstrap-server kafka:9092
#Leer mensajes de kafka
docker compose exec kafka kafka-console-consumer --topic test-topic --bootstrap-server kafka:9092 --from-beginning
