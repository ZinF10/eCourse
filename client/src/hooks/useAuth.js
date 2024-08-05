import { useCurrentUser } from "@/contexts/AuthContext";
import httpClient from "@/services/client";
import endpoints from "@/services/endpoints";
import cookie from 'react-cookies';

const useAuth = () => {
    const [, dispatch] = useCurrentUser();

    const login = async (email, password) => {
        try {
            const data = {
                email: email,
                password: password,
            };

            const response = await httpClient.post(
                endpoints['token'],
                data,
            );

            if (!response.data.access_token) {
                return false;
            }

            cookie.save(
                'access_token',
                response.data.access_token,
                { path: '/' },
            );

            const user = await httpClient.get(
                endpoints['current_user'],
                {
                    headers: {
                        Authorization: `Bearer ${cookie.load(
                            'access_token',
                        )}`,
                    },
                },
            );

            cookie.save('current_user', user.data, {
                path: '/',
            });

            dispatch({
                type: 'LOGIN',
                payload: user.data,
            });

            return true;
        } catch (error) {
            console.error('Error logging in:', error);
            return false;
        }
    };

    const logout = () => {
        dispatch({ type: 'LOGOUT' });
    };

    const isAuthenticated = () => {
        const accessToken = cookie.load('access_token');
        const currentUser = cookie.load('current_user');
        if (accessToken && currentUser) {
            return currentUser.is_doctor || currentUser.is_nurse;
        }
        return true;
    };

    return { login, logout, isAuthenticated };
}

export default useAuth