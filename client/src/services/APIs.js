import { BASE_URL } from '@/constants/constants';
import axios from 'axios';

const axiosInstance = axios.create({
	baseURL: BASE_URL,
	timeout: 3500,
	headers: {
		'Content-Type': 'application/json'
	}
});

export default axiosInstance;
