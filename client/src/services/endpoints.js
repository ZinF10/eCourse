const endpoints = {
    categories: process.env.CATEGORIES_API,
    courses: (keyword, category, latest) => {
        let url = `${process.env.COURSES_API}?`;
        if (latest) url += `latest=${latest}&`;
        if (keyword) url += `keyword=${keyword}&`;
        if (category) url += `category=${category}`;
        return url.slice(-1) === '&' ? url.slice(0, -1) : url;
    },
    course: (id) => `${process.env.COURSES_API}${id}/`,
    token: process.env.TOKEN_API,
    current_user: process.env.CURRENT_USER_API,
    register: process.env.REGISTER_API

};

export default endpoints;