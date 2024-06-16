import Each from '@/components/common/Each';
import Loading from '@/components/common/Loading';
import useFetch from '@/hooks/customs/useFetch';
import endpoints from '@/services/endpoints';
import { Link, useLocation } from 'react-router-dom';

const Courses = () => {
	const location = useLocation();
	const queryParams = new URLSearchParams(location.search);
	const category = queryParams.get('category');
	const keyword = queryParams.get('keyword');
	const { data, isLoading, error } = useFetch(
		endpoints['courses'](keyword, category),
	);

	if (isLoading) {
		return <Loading />;
	}

	if (error) {
		return <p>{error}</p>;
	}

	return (
		<section>
			<h1>Courses</h1>

			{data && data.length > 0 ? (
				<Each
					of={data}
					render={(item, index) => (
						<li key={index}>
							<Link to={`${item.id}`}>
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

export default Courses;
