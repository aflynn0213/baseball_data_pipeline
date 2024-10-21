import React, { useEffect, useState } from 'react';
import PlayerList from './components/PlayerList.jsx';
import { fetchPlayers } from './services/api';

const App = () => {
    const [players, setPlayers] = useState([]);

    useEffect(() => {
        async function loadData() {
            const playerData = await fetchPlayers();
            setPlayers(playerData);
        }
        loadData();
    }, []);

    return (
        <div className="App">
            <h1>Player Performance Dashboard</h1>
            <PlayerList players={players} />
        </div>
    );
}

export default App;
