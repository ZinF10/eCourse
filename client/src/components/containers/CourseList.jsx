import useAxios from "@/hooks/useAxios";
import endpoints from "@/services/endpoints";
import { Link, useLocation } from "react-router-dom";
import ActivityIndicator from "../common/ActivityIndicator";
import NotFound from "../common/NotFound";
import { Button, Card, Col, Row } from "react-bootstrap";
import { CiShoppingCart } from "react-icons/ci";

const CourseItem = ({ course }) => (
    <Col key={course.id} xs={12} md={6} lg={3}>
        <article className="h-100">
            <Card>
                <Link to={`/courses/${course.id}`}>
                    <Card.Img variant="top" src={course.image} />
                </Link>
                <Card.Body>
                    <Card.Title>{course.subject}</Card.Title>
                    <Card.Text>{course.category}</Card.Text>
                    <Button variant="outline-dark"><CiShoppingCart size={24} /></Button>
                </Card.Body>
            </Card>
        </article>
    </Col>
);


const CourseList = ({ isNew }) => {
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const category = queryParams.get('category');
    const keyword = queryParams.get('keyword');
    const latest = queryParams.get('latest') || isNew;
    const { data, isLoading, error } = useAxios(endpoints['courses'](keyword, category, latest))

    if (error) return <p>{error}</p>;

    return (
        <Row className="g-4">
            {isLoading ? <ActivityIndicator /> : (data && data.length > 0 ? (data.map((course) => (
                <CourseItem key={course.id} course={course} />
            ))) : <NotFound />)}
        </Row>
    )
}

export default CourseList