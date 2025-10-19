import React, { useState, useEffect } from 'react';
import { useWebSocket } from '../hooks/useWebsocket.js';
import { useYjs } from '../hooks/useYjs.js';
import TextBox from '../components/TextBox.jsx';

function Landing() {

    const { socket, isConnected, userId } = useWebSocket();
    const { yText } = useYjs();
    const [locText, setLocText] = useState('');

    useEffect(() => {
        if (yText) {
            const updateText = () => {
                setLocText(yText.toString());
            };
            yText.observe(updateText);
            return () => yText.unobserve(updateText);
        }
    }, [yText]);

    const handleChange = (e) => {
        const newText = e.target.value;
        setLocText(newText); 
        if (yText) {
            yText.delete(0, yText.length);
            yText.insert(0, newText);
        }
    };

    return (
        <div className="landing-page">
            {userId && <p style={{ marginBottom: '30px' }}>User ID: <b>{userId}</b></p>}
            <TextBox value={locText} onChange={handleChange} placeholder="Start typing..."/>
        </div>
    );
}

export default Landing;