import AuthReducer from '@/redux/reducers/AuthReducer';
import { createContext, useContext, useMemo } from 'react';
import { useReducer } from 'react';
import cookie from 'react-cookies';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const initialState = cookie.load('current_user') || null;

    const [user, dispatch] = useReducer(AuthReducer, initialState);

    const contextValue = useMemo(() => [user, dispatch], [user]);

    return (
        <AuthContext.Provider value={contextValue}>
            {children}
        </AuthContext.Provider>
    );
};

export const useCurrentUser = () => useContext(AuthContext);

export default AuthContext;