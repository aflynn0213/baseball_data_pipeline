import React from 'react';
import PlayerProfile from './PlayerProfile';

const PlayerList = ({ players }) => {
    return (
        <div>
            {players.map(player => (
                <PlayerProfile key={player.player_name} player={player} />
            ))}
        </div>
    );
}

export default PlayerList;
