def get_success_rate(success_count, total_count):
    if total_count == 0:
        return 0.0
    return (success_count / total_count) * 100

def get_min_latency(latencies):
    if not latencies:
        return 0.0
    return min(latencies)

def get_max_latency(latencies):
    if not latencies:
        return 0.0
    return max(latencies)

def get_mean_latency(latencies):
    if not latencies:
        return 0.0
    return sum(latencies) / len(latencies)

def get_p95_latency(latencies):
    if not latencies:
        return 0.0
    sorted_lats = sorted(latencies)
    p95_index = int(len(sorted_lats) * 0.95)
    return sorted_lats[p95_index]

def get_p99_latency(latencies):
    if not latencies:
        return 0.0
    sorted_lats = sorted(latencies)
    p99_index = int(len(sorted_lats) * 0.99)
    return sorted_lats[p99_index]

def get_p50_latency(latencies):
    if not latencies:
        return 0.0
    sorted_lats = sorted(latencies)
    p50_index = int(len(sorted_lats) * 0.50)
    return sorted_lats[p50_index]