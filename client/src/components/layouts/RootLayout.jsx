import { Outlet } from 'react-router-dom';
import Footer from './Footer';
import Header from './Header';

const RootLayout = () => {
	return (
		<>
			<Header />
			<main className='mx-auto max-w-screen-xl lg:py-4'>
				<Outlet />
			</main>
			<Footer />
		</>
	);
};

export default RootLayout;
