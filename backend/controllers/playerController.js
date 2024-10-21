const pool = require('../db');

const getPlayers = async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM processed_statcast');
        res.json(result.rows);
    } catch (error) {
        console.error('Error fetching players:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
};

module.exports = {
    getPlayers,
};
