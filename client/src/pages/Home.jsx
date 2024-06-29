import Greeting from '@/components/common/Greeting';
import Loading from '@/components/common/Loading';
import CourseList from '@/components/containers/CourseList';
import AuthContext from '@/hooks/contexts/AuthContext';
import useFetch from '@/hooks/customs/useFetch';
import endpoints from '@/services/endpoints';
import { useContext } from 'react';

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

			{user && (
				<Greeting username={user.username} />
			)}

			<CourseList courses={data}/>
		</section>
	);
};

export default Home;
