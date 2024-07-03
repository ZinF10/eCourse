import { useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';

const useDocumentTitle = (title, prevailOnUnmount = false) => {
    const location = useLocation();
    const defaultTitle = useRef(document.title);

    useEffect(() => {
        document.title = title;
    }, [location, title]);

    useEffect(() => () => {
        if (!prevailOnUnmount) {
            document.title = defaultTitle.current;
        }
    }, [prevailOnUnmount])
}

export default useDocumentTitle