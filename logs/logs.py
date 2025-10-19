def parse_logs():
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
                'response_time': parts[5][:-2].strip()
            }
            all_logs.append(log_entry)
        
        return all_logs


if __name__ == "__main__":
    logs = parse_logs()
    print(logs)