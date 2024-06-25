import About from '@/pages/About';
import CourseDetail from '@/pages/CourseDetail';
import Courses from '@/pages/Courses';
import Home from '@/pages/Home';
import LessonDetail from '@/pages/LessonDetail';
import LogIn from '@/pages/LogIn';
import PageNotFound from '@/pages/PageNotFound';
import Profile from '@/pages/Profile';
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
	{
		path: '/courses/:id/lessons/:lesson_id',
		component: LessonDetail,
		lazy: () => import('@/pages/LessonDetail'),
	},
	{
		path: '/profile',
		component: Profile,
		lazy: () => import('@/pages/Profile'),
	},
	{
		path: '*',
		component: PageNotFound,
		lazy: () => import('@/pages/PageNotFound'),
	},
];

export default routes;
