import { Route, Routes } from 'react-router-dom';
import routes from '@/routes/routes';
import RootLayout from '@/components/layouts/RootLayout';

const App = () => {
	return (
		<Routes>
			<Route element={<RootLayout />}>
				{routes.map((route) => {
					const Page = route.component;
					return (
						<Route
							key={route}
							path={route.path}
							element={<Page />}
							lazy={route.lazy}
						/>
					);
				})}
			</Route>
		</Routes>
	);
};

export default App;
