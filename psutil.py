import psutil
def monitoreo_sistema():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    return {
        "cpu": cpu_usage,
        "memory": memory_info.percent
    }
metricas = monitoreo_sistema()
print(f"Uso de CPU: {metricas['cpu']}%")
print(f"Uso de Memoria: {metricas['memory']}%")
