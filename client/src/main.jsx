import React, { Suspense } from 'react'
import ReactDOM from 'react-dom/client'
import 'bootstrap/dist/css/bootstrap.min.css';
import App from '@/App';
import { Provider } from 'react-redux';
import { store } from '@/redux/store';
import Loading from './components/ui/atoms/Loading';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Suspense fallback={<Loading />}>
      <Provider store={store}>
        <App />
      </Provider>
    </Suspense>
  </React.StrictMode>
)
