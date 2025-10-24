import React, { useState, useEffect } from 'react';
import { useWebSocket } from '../hooks/useWebsocket.js';
import TextBox from '../components/TextBox.jsx';

function Landing() {

    const { socket, isConnected, userId } = useWebSocket();

    return (
        <div className="landing-page">
            {userId && <p style={{ marginBottom: '30px' }}>User ID: <b>{userId}</b></p>}
        </div>
    );
}

export default Landing;