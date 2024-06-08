import About from '@/pages/About';
import CourseDetail from '@/pages/CourseDetail';
import Courses from '@/pages/Courses';
import Home from '@/pages/Home';
import LogIn from '@/pages/LogIn';
import Register from '@/pages/Register';

const routes = [
	{
		path: '/',
		exact: true,
		component: Home,
		lazy: () => import('@/pages/Home'),
	},
	{
		path: '/about',
		component: About,
		lazy: () => import('@/pages/About'),
	},
	{
		path: '/login',
		exact: true,
		component: LogIn,
		lazy: () => import('@/pages/LogIn'),
	},
	{
		path: '/register',
		component: Register,
		lazy: () => import('@/pages/Register'),
	},
	{
		path: '/courses',
		component: Courses,
		lazy: () => import('@/pages/Courses'),
	},
	{
		path: '/courses/:id',
		component: CourseDetail,
		lazy: () => import('@/pages/CourseDetail'),
	},
];

export default routes;
