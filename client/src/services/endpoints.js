import {
	CATEGORIES_API,
	COURSES_API,
	CURRENT_USER_API,
	REGISTER_API,
	TOKEN_API,
} from '@/constants/constants';

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
	course_detail: (id) => `${COURSES_API}${id}/`,
	lessons_course: (id) => `${COURSES_API}${id}/lessons/`,
	register: REGISTER_API,
	token: TOKEN_API,
	current_user: CURRENT_USER_API,
};

export default endpoints;
