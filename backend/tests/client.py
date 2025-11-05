import socketio


def make_client():
    sio = socketio.Client()

    @sio.on('metrics_response')
    def handle_metrics_response(data):
        print_time_metrics(data['time'])
        print_count_metrics(data['count'], data['time']['duration'])
        print_concurrency_metrics(data['concurrency'])

    return sio


def print_time_metrics(time_data):
    print("\n=== Time Metrics ===")
    print(f"Duration: {time_data['duration']:.4f}s")
    print(f"Min Latency: {time_data['min_latency']:.6f}ms")
    print(f"Max Latency: {time_data['max_latency']:.6f}ms")
    print(f"Mean Latency: {time_data['mean_latency']:.6f}ms")
    print(f"P50 Latency: {time_data['p50_latency']:.6f}ms")
    print(f"P95 Latency: {time_data['p95_latency']:.6f}ms")
    print(f"P99 Latency: {time_data['p99_latency']:.6f}ms")


def print_count_metrics(count_data, duration):
    print("\n=== Count Metrics ===")
    print(f"Total Requests: {count_data['total_requests']}")
    print(f"SET Success: {count_data['set_success']}")
    print(f"SET Failure: {count_data['set_failure']}")

    throughput = count_data['total_requests'] / duration
    print(f"Throughput: {throughput:.2f} req/s")


def print_concurrency_metrics(concurrency_data):
    print("\n=== Concurrency Metrics ===")
    print(f"Peak Concurrent: {concurrency_data['peak_concurrent']}")
    print(f"Min Concurrent: {concurrency_data['min_concurrent']}")
    print(f"Mean Concurrent: {concurrency_data['mean_concurrent']:.2f}")
    print(f"Std Dev Concurrent: {concurrency_data['std_dev_concurrent']:.2f}")
    print(f"P50 Concurrent: {concurrency_data['p50_concurrent']}")
    print(f"P95 Concurrent: {concurrency_data['p95_concurrent']}")
    print(f"P99 Concurrent: {concurrency_data['p99_concurrent']}")
    print(f"Contention Rate: {concurrency_data['contention_rate']:.2f}%")