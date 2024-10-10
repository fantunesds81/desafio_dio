import psutil

# obter informação de uso da cpu

cpu_percent = psutil.cpu_percent()
print(f'Uso da CPU: {cpu_percent}%')

# obter informação de uso de memória

memory = psutil.virtual_memory()
print(f'Uso de memória: {memory.percent}%')

# obter informção de uso do disco
disk_usage = psutil.disk_usage("/")
print(f'Uso de disco: {disk_usage.percent}%')


# obter lista de processos
processes = psutil.process_iter()
for process in processes:
    print(f"PID: {process.pid}, Nome: {process.name()}")