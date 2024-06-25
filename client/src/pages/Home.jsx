import Greeting from '@/components/common/Greeting';
import CourseList from '@/components/containers/CourseList';
import AuthContext from '@/hooks/contexts/AuthContext';
import { useContext } from 'react';

const Home = () => {
	const [user] = useContext(AuthContext);

	return (
		<section>
			<h1>Home</h1>

			{user && (
				<Greeting username={user.username} />
			)}

			<CourseList />
		</section>
	);
};

export default Home;
