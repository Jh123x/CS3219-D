echo Setting up topics
python ./kafka_admin.py
echo Launching Consumer
start python ./kafka_consumer.py
echo Viewing container description
view_master.bat
