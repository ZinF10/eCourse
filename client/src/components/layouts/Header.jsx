import { Link, useNavigate } from 'react-router-dom';
import { Each } from '../common/Each';
import endpoints from '@/services/endpoints';
import useFetch from '@/hooks/useFetch';
import { Loading } from '../common/Loading';

const Header = () => {
	const { data, isLoading, error } = useFetch(endpoints['categories']);
	const navigate = useNavigate();

	if (isLoading) {
		return <Loading />;
	}

	if (error) {
		return <p>{error}</p>;
	}

	const handleSubmit = (event) => {
		event.preventDefault();
		let params = serializeFormQuery(event.target);
		navigate(`courses?${params}`);
	};

	const serializeFormQuery = (form) => {
		const formData = new FormData(form);
		let params = new URLSearchParams();
		for (let [key, value] of formData.entries()) {
			params.append(key, value);
		}
		return params.toString();
	};

	return (
		<header>
			{data ? (
				<>
					<ul>
						<li>
							<Link to={'/'}>
								Home
							</Link>
						</li>
						<Each
							of={data}
							render={(
								item,
								index,
							) => (
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
							<Link to={'/about'}>
								About
							</Link>
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

					<form onSubmit={handleSubmit}>
						<input
							type='text'
							name='keyword'
							placeholder='Search...'
						/>
						<button type='submit'>
							Search
						</button>
					</form>
				</>
			) : (
				<p>No data exists...</p>
			)}
		</header>
	);
};

export default Header;
