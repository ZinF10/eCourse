import axios from "axios";

const httpClient = axios.create({
    baseURL: process.env.API_BASE_URL,
    timeout: 3500,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default httpClient