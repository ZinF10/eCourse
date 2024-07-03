import AuthContext from '@/hooks/contexts/AuthContext';
import AuthReducer from '@/redux/reducers/AuthReducer';
import { useReducer } from 'react';
import cookie from 'react-cookies';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import RootLayout from '../layouts/RootLayout';
import { PrivateRoutes, PublicRoutes } from '@/routes/routes';
import PrivateRoute from './PrivateRoute';
import { ThemeProvider } from '@material-tailwind/react';

const RootNavigatiors = () => {
    let current = cookie.load('current_user');
    if (current === undefined) current = null;

    const [user, dispatch] = useReducer(AuthReducer, current);

    return (
        <BrowserRouter>
            <AuthContext.Provider value={[user, dispatch]}>
                <ThemeProvider>
                    <Routes>
                        <Route element={<RootLayout />}>
                            {PublicRoutes.map((route) => {
                                const Page =
                                    route.component;
                                return (
                                    <Route
                                        key={
                                            route
                                        }
                                        path={
                                            route.path
                                        }
                                        element={
                                            <Page />
                                        }
                                        lazy={
                                            route.lazy
                                        }
                                    />
                                );
                            })}
                            <Route element={<PrivateRoute />}>
                                {PrivateRoutes.map((route) => {
                                    const Page = route.component;
                                    return (
                                        <Route
                                            key={route.path}
                                            path={route.path}
                                            element={<Page />}
                                        />
                                    );
                                })}
                            </Route>
                        </Route>
                    </Routes>
                </ThemeProvider>
            </AuthContext.Provider>
        </BrowserRouter>
    );
};

export default RootNavigatiors