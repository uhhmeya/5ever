import socketio

def make_admin():
    sio = socketio.Client()

    @sio.on('metrics_response')
    def handle_metrics_response(data):
        print(f"Total Set Requests: {data['total_set']}")
        print(f"Total Operations: {data['total_operations']}")
        print(f"Success Rate: {data['success_rate']:.2f}%")
        print(f"Duration: {data['duration']:.2f}s")
        print(f"Throughput: {data['throughput']:.2f} ops/sec\n")
        print(f"Min Latency: {data['min_latency']:.2f}ms")
        print(f"Max Latency: {data['max_latency']:.2f}ms")
        print(f"Mean Latency: {data['mean_latency']:.2f}ms")
        print(f"P50 Latency: {data['p50_latency']:.2f}ms")
        print(f"P95 Latency: {data['p95_latency']:.2f}ms")
        print(f"P99 Latency: {data['p99_latency']:.2f}ms")

    return sio