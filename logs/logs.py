def parse_logs() -> list:
    with open('input/access.log', 'r') as file:
        lines = file.readlines()
        
        all_logs = []
        
        for line in lines:
            parts = line.split(',')
            log_entry = {
                'timestamp': parts[0].strip(),
                'level': parts[1].strip(),
                'ip': parts[2].strip(),
                'endpoint': parts[3].strip(),
                'status': parts[4].strip(),
                'response_time': parts[5][:-3].strip()
            }
            all_logs.append(log_entry)
        
        return all_logs

def count_logs(logs: list) -> int:
    return len(logs)

def count_errors(logs: list) -> int:
    
    errors = 0
   
    for log in logs:
        status = log['status']
        
        if status.startswith('4') or status.startswith('5'):
            errors += 1
  
    return errors

def top_endpoints(logs: list, n: int = 5) -> list:
    endpoint_count = {}
    
    for log in logs:
        endpoint = log['endpoint']
        
        if endpoint in endpoint_count:
            endpoint_count[endpoint] += 1
        else:
            endpoint_count[endpoint] = 1
    
    sorted_endpoints = sorted(endpoint_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_endpoints[:n]

def average_response_time(logs:list) -> float:
    total_time = 0.0
    
    for log in logs:
        response_time = float(log['response_time'])
        total_time += response_time
    
    average_time = total_time / len(logs) if logs else 0.0
    
    return average_time

def mocst_common_ip(logs: list) -> str:
    ip_count = {}

    for log in logs:
        ip = log['ip']
        
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1
        
    most_common_ip = max(ip_count, key=ip_count.get)
    
    return most_common_ip

def status_distribution(logs: list) -> dict:
    status_count = {}
    
    for log in logs:
        status = log['status']
        
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1
    
    return status_count

if __name__ == "__main__":
    logs = parse_logs()
    total_logs = count_logs(logs)
    total_errors = count_errors(logs)
    top_5_endpoints = top_endpoints(logs, 5)
    average_time = average_response_time(logs)
    most_common_ip = mocst_common_ip(logs)
    distribution_of_status = status_distribution(logs)

    print(f"Statystyki:")
    print(f"Wszystkich żądań: {total_logs}")
    print(f"Żądań z błędem: {total_errors}")
    print(f"\nTop 5 endpointów:")
    for endpoint, count in top_5_endpoints:
        print(f"  {endpoint}: {count} razy")
    print(f"\nŚredni czas odpowiedzi: {average_time:.2f} ms")
    print(f"Najczęściej występujące IP: {most_common_ip}")
    print(f"\nRozkład statusów:")
    for status, count in distribution_of_status.items():
        print(f"  {status}: {count} razy")