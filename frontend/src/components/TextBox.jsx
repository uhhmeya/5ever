import React from 'react';
import '../styles/textbox.css'

function TextBox({ value, onChange, placeholder = "Start typing here..." }) {
    return (
        <div className="textbox-container">
            <textarea
                className="textbox"
                value={value}
                onChange={onChange}
                placeholder={placeholder}
            />
        </div>
    );
}

export default TextBox;