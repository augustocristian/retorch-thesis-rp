import json
import csv
from datetime import datetime

# URL de tu instancia de Prometheus y consulta filtrada por el ID "/"

prometheus_url = 'http://156.35.119.57:9090/api/v1/query'


# http://156.35.119.57:9090/api/v1/query_range?query=rate(container_cpu_usage_seconds_total{id="/"}[1m])&start=1727513399&end=1727515259&step=1
# http://156.35.119.57:9090/api/v1/query_range?query=container_memory_usage_bytes{id="/"}/1024/1024/1024&start=1727513399&end=1727515259&step=1


# Función para convertir la marca de tiempo Unix a una fecha y hora legible
def unix_to_datetime(unix_timestamp):
    return datetime.utcfromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')


def saveinCSVData(routeinput, routeoutput):
    # Load the JSON data
    with open(routeinput) as f:
        data = json.load(f)

    # Extract the results
    results = data['data']['result']

    # Open a CSV file for writing
    with open(routeoutput, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['timestamp', 'value'])

        # Iterate through the data points and write to CSV
        for result in results:
            for value in result['values']:
                timestamp, usage_value = value
                usage_value_comma = str(usage_value).replace('.', ',')
                writer.writerow([ unix_to_datetime(timestamp), usage_value_comma])


saveinCSVData("data/MemoryBaseline.json", "BaseLineMemory.csv")
saveinCSVData("data/CPUbaseline.json", "BaselineCPU.csv")

print('Datos de uso de Memoria exportados a memory_usage_last_2h.csv')
