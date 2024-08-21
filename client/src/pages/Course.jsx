import useAxios from "@/hooks/useAxios";
import endpoints from "@/services/endpoints";
import { useParams } from "react-router-dom";
import { Button, Card, Col, Container, Form, Row } from "react-bootstrap";
import ActivityIndicator from "@/components/ui/atoms/ActivityIndicator";
import NoMatch from "@/components/ui/atoms/NoMatch";

const Course = () => {
    const { id } = useParams();
    const { data, isLoading, error } = useAxios(endpoints['course'](id))

    if (error) console.error(error)

    return (
        <Container>
            <Row className="my-4">
                {isLoading ? <ActivityIndicator /> : (data ? (<>
                    <Col md={8}>
                        <Card>
                            <Card.Img variant="top" src={data.image || 'https://via.placeholder.com/600x400'} />
                            <Card.Body>
                                <Card.Title>{data.title}</Card.Title>
                                <Card.Text>{data.description}</Card.Text>
                                <Button variant="primary">Try Now</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={4}>
                        <Card>
                            <Card.Body>
                                <h5>Comments</h5>
                                <ul className="list-unstyled">
                                </ul>
                                <Form>
                                    <Form.Group controlId="commentForm">
                                        <Form.Label>Write your comment</Form.Label>
                                        <Form.Control
                                            as="textarea"
                                            rows={3}
                                        />
                                    </Form.Group>
                                    <Button variant="primary" type="submit" className="mt-2">
                                        Send
                                    </Button>
                                </Form>
                            </Card.Body>
                        </Card>
                    </Col>
                </>) : <NoMatch />)}
            </Row>
        </Container>
    );
}

export default Course