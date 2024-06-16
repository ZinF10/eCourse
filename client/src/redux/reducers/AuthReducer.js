import cookie from 'react-cookies';
import axiosInstance from '@/services/APIs';

const initialState = {
	accessToken: null,
};

const AuthReducer = (state = initialState, action) => {
	switch (action.type) {
		case 'LOGIN':
			return action.payload;
		case 'LOGOUT':
			cookie.remove('access_token');
			cookie.remove('current_user');
			axiosInstance.defaults.headers['Authorization'] = null;
			return null;
		default:
			return state;
	}
};

export default AuthReducer;
