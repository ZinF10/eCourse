import Each from '@/components/common/Each';
import Greeting from '@/components/common/Greeting';
import Loading from '@/components/common/Loading';
import AuthContext from '@/hooks/contexts/AuthContext';
import useFetch from '@/hooks/customs/useFetch';
import endpoints from '@/services/endpoints';
import { useContext } from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
	const [user] = useContext(AuthContext);
	const { data, isLoading, error } = useFetch(endpoints['courses']());

	if (isLoading) {
		return <Loading />;
	}

	if (error) {
		return <p>{error}</p>;
	}

	return (
		<section>
			<h1>Home</h1>

			{user ? (
				<Greeting username={user.username} />
			) : (
				<Loading />
			)}

			{data ? (
				<Each
					of={data}
					render={(item, index) => (
						<li key={index}>
							<Link
								to={`courses/${item.id}`}>
								{item.subject}
							</Link>
							<p>
								Price: $
								{item.price}
							</p>
							<p>
								Category:{' '}
								<i>
									{
										item.category
									}
								</i>
							</p>
						</li>
					)}
				/>
			) : (
				<p>No items exists</p>
			)}
		</section>
	);
};

export default Home;
