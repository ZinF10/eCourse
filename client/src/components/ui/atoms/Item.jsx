import { Link } from "react-router-dom";
import { Card, Col } from "react-bootstrap";
import { CiShoppingCart } from "react-icons/ci";
import Button from "./Button";

const Item = ({ course }) => (
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

export default Item;