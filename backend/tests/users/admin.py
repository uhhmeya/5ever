import socketio

def make_admin():
    sio = socketio.Client()

    @sio.on('metrics_response')
    def handle_metrics_response(data):

        print("\n=== Time Metrics ===")
        print(f"Duration: {data['time']['duration']:.4f}s")
        print(f"Min Latency: {data['time']['min_latency']:.6f}ms")
        print(f"Max Latency: {data['time']['max_latency']:.6f}ms")
        print(f"Mean Latency: {data['time']['mean_latency']:.6f}ms")
        print(f"P50 Latency: {data['time']['p50_latency']:.6f}ms")
        print(f"P95 Latency: {data['time']['p95_latency']:.6f}ms")
        print(f"P99 Latency: {data['time']['p99_latency']:.6f}ms")

        print("\n=== Count Metrics ===")
        print(f"Total Requests: {data['count']['total_requests']}")
        print(f"SET Success: {data['count']['set_success']}")
        print(f"SET Failure: {data['count']['set_failure']}")

        duration = data['time']['duration']
        total_requests = data['count']['total_requests']
        throughput = total_requests / duration
        print(f"Throughput: {throughput:.2f} req/s")

    return sio