const { Pool } = require('pg');
const pool = new Pool({
    user: 'yourUsername',
    host: 'localhost',
    database: 'baseball',
    password: 'yourPassword',
    port: 5432,
});

module.exports = pool;
