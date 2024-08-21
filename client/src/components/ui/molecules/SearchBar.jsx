import { Form } from 'react-bootstrap'

const SearchBar = ({ navigate }) => {
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
        <Form className="d-flex mb-3 mb-lg-0 me-lg-3" onSubmit={handleSubmit}>
            <Form.Control
                type="search"
                placeholder="Search for anything"
                aria-label="Search for anything"
                name='keyword'
            />
        </Form>
    )
}

export default SearchBar