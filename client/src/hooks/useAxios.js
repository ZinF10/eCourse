import httpClient from '@/services/client';
import { useCallback, useEffect, useState } from 'react';

const useAxios = (url) => {
    const [data, setData] = useState(null);
    const [isLoading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchData = useCallback(async () => {
        try {
            setLoading(true);
            const response = await httpClient.get(url);
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

export default useAxios