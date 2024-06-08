import { Loading } from '@/components/common/Loading';
import useFetch from '@/hooks/useFetch';
import endpoints from '@/services/endpoints';
import { useParams } from 'react-router-dom';

const CourseDetail = () => {
	const { id } = useParams();

	const { data, isLoading, error } = useFetch(
		endpoints['course_detail'](id),
	);

	if (isLoading) {
		return <Loading />;
	}

	if (error) {
		return <p>{error}</p>;
	}

	return (
		<section>
			<h1>Course Detail</h1>
			{data ? (
				<ul>
					<li>{data.subject}</li>
					<li>Description: {data.description}</li>
					<li>Price: ${data.price}</li>
					<li>Category: {data.category}</li>
				</ul>
			) : (
				<p>No items</p>
			)}
		</section>
	);
};

export default CourseDetail;
