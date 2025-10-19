import { useEffect, useState } from 'react';
import { socket } from '../utils/socket.js';
import { obtainUserID } from "../utils/userID.js";

export function useWebSocket() {

    const [isConnected, setIsConnected] = useState(false);
    const [userId, setUserId] = useState(null);

    useEffect(() => {

        socket.on('connect', () => {
            setIsConnected(true);
            const id = obtainUserID();
            setUserId(id);
            socket.emit('user_id', { userId: id });
        });

        socket.on('disconnect', () => setIsConnected(false));

        return () => {
            socket.off('connect');
            socket.off('disconnect');
        };
    }, []);

    return { socket, isConnected, userId };
}