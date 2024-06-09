import { CATEGORIES_API, COURSES_API, REGISTER_API } from '@/constants/constants';

const endpoints = {
	categories: CATEGORIES_API,
	courses: (keyword, category) => {
		let url = `${COURSES_API}?`;
		if (keyword) {
			url += `keyword=${keyword}&`;
		}
		if (category) {
			url += `category=${category}`;
		}
		return url;
	},
	course_detail: (id) => `${COURSES_API}${id}`,
	register: REGISTER_API,
};

export default endpoints;
