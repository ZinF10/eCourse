import { Link } from 'react-router-dom';
import { Each } from '../common/Each';
import endpoints from '@/services/endpoints';
import useFetch from '@/hooks/useFetch';
import { Loading } from '../common/Loading';

const Header = () => {
	const { data, isLoading, error } = useFetch(endpoints['categories']);

	if (isLoading) {
		return <Loading />;
	}

	if (error) {
		return <p>{error}</p>;
	}

	return (
		<header>
			{data ? (
				<ul>
					<li>
						<Link to={'/'}>Home</Link>
					</li>
					<Each
						of={data}
						render={(item, index) => (
							<li key={index}>
								<Link
									to={`courses/?category=${item.id}`}>
									{
										item.name
									}
								</Link>
							</li>
						)}
					/>
					<li>
						<Link to={'/about'}>About</Link>
					</li>
					<li>
						<Link to={'/login'}>
							Log In
						</Link>
					</li>
					<li>
						<Link to={'/register'}>
							Register
						</Link>
					</li>
				</ul>
			) : (
				<p>No data exists...</p>
			)}
		</header>
	);
};

export default Header;
