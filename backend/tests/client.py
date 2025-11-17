import socketio

def make_client():
    sio = socketio.Client()
    sio.connect('http://localhost:5003')

    @sio.on('response')
    def hres(data):
        print(f"    Latency: min={data['minL']:.1f} max={data['maxL']:.1f} mean={data['meanL']:.1f} p50={data['p50L']:.1f} p95={data['p95L']:.1f} p99={data['p99L']:.1f} ms")
        print(f"    Count: r={data['totalR']} dur={data['dur']:.1f}s tput={data['totalR']/data['dur']:.1f}r/s")
        print(f"    Concurrency: peak={data['peak']} min={data['minC']} mean={data['meanC']:.1f} p50={data['p50C']} p95={data['p95C']} p99={data['p99C']} conten={data['conten']:.1f}% \n")

    return sio