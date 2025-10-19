import matplotlib.pyplot as plt

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

    report = "Log Report\n"
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

def plot_status_distribution(status_dist: dict):
    statuses = list(status_dist.keys())
    counts = list(status_dist.values())

    plt.figure(figsize=(10, 6))
    plt.bar(statuses, counts, color='skyblue')
    plt.xlabel('Status Codes')
    plt.ylabel('Number of Occurrences')
    plt.title('Status Code Distribution')
    plt.savefig('output/status_distribution.png')
    plt.close()

def plot_top_endpoints(logs: list, n: int = 5):
    top_5 = top_endpoints(logs, n)
    endpoints = [item[0] for item in top_5]
    counts = [item[1] for item in top_5]

    plt.figure(figsize=(10, 6))
    plt.bar(endpoints, counts, color='lightgreen')
    plt.xlabel('Endpoints')
    plt.ylabel('Number of Hits')
    plt.title(f'Top {n} Endpoints')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/top_endpoints.png')
    plt.close()

def main():
    logs = parse_logs()
    report = generate_report(logs)

    print(report)

    with open('output/report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(report)

    status_dist = status_distribution(logs)
    plot_status_distribution(status_dist)
    plot_top_endpoints(logs, 5)

if __name__ == "__main__":
    main()