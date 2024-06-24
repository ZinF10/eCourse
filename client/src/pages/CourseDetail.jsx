import Each from '@/components/common/Each';
import Loading from '@/components/common/Loading';
import useFetch from '@/hooks/customs/useFetch';
import endpoints from '@/services/endpoints';
import { Link, useParams } from 'react-router-dom';

const CourseDetail = () => {
	const { id } = useParams();

	const { data: detail, isLoading, error } = useFetch(
		endpoints['course_detail'](id),
	);

	const { data: lessons } = useFetch(
		endpoints['lessons_course'](id),
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
			{detail ? (
				<>
					<ul>
						<li>{detail.subject}</li>
						<li>Description: {detail.description}</li>
						<li>Price: ${detail.price}</li>
						<li>Category: {detail.category}</li>
					</ul>
					{lessons ? (<Each
						of={lessons}
						render={(item, index) => (
							<ul key={index}>
								<li>
									<Link
										to={`courses/${item.id}`}>
										{item.subject}
									</Link>
								</li>
							</ul>
						)}
					/>) : <p>No items</p>}
				</>
			) : (
				<p>No items</p>
			)}
		</section>
	);
};

export default CourseDetail;
