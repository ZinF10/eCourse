import { Outlet, Navigate } from 'react-router-dom';
import cookie from 'react-cookies';

const PrivateRoute = () => {
    const isAuthenticated = () => {
        const accessToken = cookie.load('access_token');
        const currentUser = cookie.load('current_user');
        return accessToken && currentUser;
    };

    return isAuthenticated() ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRoute