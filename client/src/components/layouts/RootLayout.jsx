import { Outlet } from 'react-router-dom';
import Footer from './Footer';
import Header from './Header';

const RootLayout = () => {
	return (
		<>
			<Header />
			<main className='mx-auto max-w-screen-xl p-2 lg:p-4 max-h-screen'>
				<Outlet />
			</main>
			<Footer />
		</>
	);
};

export default RootLayout;
