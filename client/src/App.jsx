import { BrowserRouter, Route, Routes } from 'react-router-dom';
import routes from '@/routes/routes';
import RootLayout from '@/components/layouts/RootLayout';
import cookie from 'react-cookies';
import { useReducer } from 'react';
import AuthReducer from './redux/reducers/AuthReducer';
import AuthContext from './hooks/contexts/AuthContext';

const App = () => {
	let current = cookie.load('current_user');
	if (current === undefined) current = null;

	const [user, dispatch] = useReducer(AuthReducer, current);

	return (
		<BrowserRouter>
			<AuthContext.Provider value={[user, dispatch]}>
				<Routes>
					<Route element={<RootLayout />}>
						{routes.map((route) => {
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
					</Route>
				</Routes>
			</AuthContext.Provider>
		</BrowserRouter>
	);
};

export default App;
