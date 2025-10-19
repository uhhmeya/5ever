import * as Y from 'yjs'
import { WebsocketProvider } from 'y-websocket'
import { useState, useEffect } from 'react'
import { obtainUserID } from '../utils/userID.js'

export function useYjs() {

    const [doc] = useState(new Y.Doc());
    const sharedPage = doc.getText('shared');
    const [yText] = useState(sharedPage);

    useEffect(() => {
        const userId = obtainUserID();

        const provider = new WebsocketProvider(
            'ws://localhost:1234',
            'main',
            doc
        );

        return () => provider.destroy();
    }, [doc]);

    return { yText };
}