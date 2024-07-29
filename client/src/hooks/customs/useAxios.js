import axiosInstance from '@/services/APIs';
import { useCallback, useEffect, useState } from 'react';
import cookie from 'react-cookies';

const useAxios = (url) => {
	const [data, setData] = useState(null);
	const [isLoading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	const fetchData = useCallback(async () => {
		try {
			setLoading(true);
			const response = await axiosInstance.get(url, {
				headers: {
					Authorization: `Bearer ${cookie.load(
						'access_token',
					)}`,
				},
			});
			setData(response.data.results || response.data);
			setError(null);
		} catch (error) {
			setError(error.message || 'Something went wrong');
		} finally {
			setLoading(false);
		}
	}, [url]);

	useEffect(() => {
		fetchData();
	}, [fetchData]);

	return { data, error, isLoading };
};

export default useAxios;
