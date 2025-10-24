import { useEffect, useState } from 'react';
import { socketio } from '../utils/socketio.js';
import { obtainUserID } from "../utils/userID.js";

export function useWebSocket() {

    const [isConnected, setIsConnected] = useState(false);
    const [userId, setUserId] = useState(null);

    useEffect(() => {

        socketio.on('connect', () => {
            setIsConnected(true);
            const id = obtainUserID();
            setUserId(id);
            socketio.emit('user_id', { userId: id });
        });

        socketio.on('disconnect', () => setIsConnected(false));

        return () => {
            socketio.off('connect');
            socketio.off('disconnect');
        };
    }, []);

    return { socket: socketio, isConnected, userId };
}