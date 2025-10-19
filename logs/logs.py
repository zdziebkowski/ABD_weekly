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

def most_common_ip(logs: list) -> str:
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

def generate_report(logs: list) -> str:
    total_logs = count_logs(logs)
    total_errors = count_errors(logs)
    top_5 = top_endpoints(logs, 5)
    avg_time = average_response_time(logs)
    top_ip = most_common_ip(logs)
    status_dist = status_distribution(logs)

    report = "Log Report"
    report += "=" *50 + "\n\n"
    report += f"Total log entries: {total_logs}\n"
    report += f"Total error entries: {total_errors}\n\n"
    report += "Top 5 Endpoints:\n"
    for endpoint, count in top_5:
        report += f"  {endpoint}: {count} hits\n"
    report += f"\nAverage Response Time: {avg_time:.2f} ms\n"
    report += f"Most Common IP: {top_ip}\n\n"
    report += "Status Code Distribution:\n"
    for status, count in status_dist.items():
        report += f"  {status}: {count} occurrences\n"
    
    return report

if __name__ == "__main__":
    logs = parse_logs()
    report = generate_report(logs)

    print(report)

    with open('output/report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(report)