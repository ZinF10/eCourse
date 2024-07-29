import useSWR from 'swr';
import axiosInstance from '@/services/axiosInstance';

const fetcher = url => axiosInstance.get(url).then(res => res.data.results)

const useFetch = (url) => {
    const { data, error, isLoading } = useSWR(url, fetcher);

    return {
        data,
        error,
        isLoading
    };
};

export default useFetch;
