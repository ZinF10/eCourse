import { Container, Spinner } from "react-bootstrap"

const Loading = () => {
    return (
        <Container style={{ width: '100vw', height: '100vh' }} className='d-flex justify-content-center align-items-center'>
            <Spinner animation="border" role="status">
                <span className="visually-hidden">Loading...</span>
            </Spinner>
        </Container>
    )
}

export default Loading