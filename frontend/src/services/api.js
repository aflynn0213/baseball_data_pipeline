export const fetchPlayers = async () => {
    try {
        const response = await fetch('http://localhost:5000/api/players');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching players:', error);
    }
};
