import React from 'react';

const PlayerProfile = ({ player }) => {
    return (
        <div className="player-profile">
            <h2>{player.player_name}</h2>
            <p>Launch Speed: {player.launch_speed}</p>
            <p>Launch Angle: {player.launch_angle}</p>
            <p>Hit Distance: {player.hit_distance}</p>
            <p>Team: {player.player_team}</p>
        </div>
    );
}

export default PlayerProfile;
