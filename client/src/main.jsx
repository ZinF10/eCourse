import React from 'react';
import ReactDOM from 'react-dom/client';
import App from '@/App';
import '@/assets/styles/global.css';
import { Provider } from 'react-redux';
import { store } from '@/redux/store';
import Loading from '@/components/common/Loading';

const root = document.getElementById('root')

ReactDOM.createRoot(root).render(
	<React.StrictMode>
		<React.Suspense fallback={<Loading />}>
			<Provider store={store}>
				<App />
			</Provider>
		</React.Suspense>
	</React.StrictMode>,
);
