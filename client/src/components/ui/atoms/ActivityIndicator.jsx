import { Container, Spinner } from "react-bootstrap"

const ActivityIndicator = () => {
    return (
        <Container style={{ width: '100vw', height: '80vh' }} className='d-flex justify-content-center align-items-center'>
            <Spinner animation="border" role="status" size="sm">
                <span className="visually-hidden">Loading...</span>
            </Spinner>
            <span className='ms-2'>Loading, please wait . . .</span>
        </Container>
    )
}

export default ActivityIndicator