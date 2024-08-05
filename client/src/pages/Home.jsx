import Hero from "@/components/common/Hero"
import CourseList from "@/components/containers/CourseList"
import { Card, Col, Row } from "react-bootstrap"
import { Link } from "react-router-dom"

const Home = () => {
    return (
        <>
            <section aria-labelledby="heros">
                <Hero />
            </section>
            <hr className='divider py-2'></hr>
            <section className="py-2" aria-labelledby="featured-courses">
                <h2 id="featured-courses">Latest Courses</h2>
                <CourseList isNew="true" />
            </section>
            <hr className='divider py-2'></hr>
            <section className="py-2" aria-labelledby="about-us">
                <h2 id="about-us">About Us</h2>
                <Row className='align-items-center'>
                    <Col md={6}>
                        <p className='text-body-tertiary'><strong className="text-dark">eCourse</strong> is a leading online learning platform with thousands of high-quality courses. We are committed to providing the best learning experience for our students.</p>
                    </Col>
                    <Col md={6}>
                        <Card className='border-0'>
                            <Card.Body>
                                <Card.Title>Contact</Card.Title>
                                <Card.Text>Email: <Link to="mailto:ecourse@gmail.com">ecourse@gmail.com</Link></Card.Text>
                                <Card.Text>Tel: <Link to="tel:+8423456789">+84 456 789</Link></Card.Text>
                                <Card.Text>Address: 777 Ong Ich Khiem, Ho Chi Minh, Viet Nam</Card.Text>
                                <Card.Text>Business Hours: Mon-Fri, 9am - 6pm</Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </section>
            <hr className='divider py-2'></hr>
        </>
    )
}

export default Home