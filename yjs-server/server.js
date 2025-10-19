import { WebSocketServer } from 'ws'
import { setupWSConnection } from '@y/websocket-server/utils'

const wss = new WebSocketServer({ port: 1234 })

wss.on('connection', (ws, request) => {
    console.log('Client joined room:', request.url)

    setupWSConnection(ws, request)

    ws.on('close', () => {
        console.log('Client left room')
    })
})

console.log(`Yjs WebSocket server running on port 1234`)