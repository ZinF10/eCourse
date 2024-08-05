import RootLayout from "@/components/layouts/RootLayout"
import { Route, Routes } from "react-router-dom";
import { PrivateRoutes, PublicRoutes } from "./routes/routes";
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from '@/contexts/AuthContext';
import PrivateRoute from "@/components/auth/PrivateRoute";


const Root = () => {
    return (
        <BrowserRouter>
            <AuthProvider>
                <Routes>
                    <Route element={<RootLayout />}>
                        {PublicRoutes.map((route) => {
                            const Page = route.component;
                            return (
                                <Route
                                    key={route}
                                    path={route.path}
                                    element={<Page />}
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
            </AuthProvider>
        </BrowserRouter>
    )
}


const App = () => {
    return (
        <Root />
    )
}

export default App