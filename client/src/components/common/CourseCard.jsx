import { Link } from "react-router-dom"
import PropTypes from 'prop-types';
import { formatPrice } from "@/utils/format";
import { Button, Card, CardBody, CardFooter, CardHeader, Typography } from "@material-tailwind/react";

const CourseCard = ({ item }) => {
    return (
        <>
            <Card className="m-3 w-80">
                <Link
                    to={`courses/${item.id}`}>
                    <CardHeader color="blue-gray" className="relative h-30">
                        <img
                            src={item.image}
                            alt={item.subject}
                        />
                    </CardHeader>
                </Link>
                <CardBody>
                    <div className="mb-2 flex items-center justify-between">
                        <Typography color="blue-gray" className="font-medium">
                            {item.subject}
                        </Typography>
                        <Typography color="blue-gray" className="font-medium">
                            {formatPrice(item.price)}
                        </Typography>
                    </div>
                </CardBody>
                <CardFooter className="pt-0 flex justify-between">
                    <Button>Read More</Button>
                    <Button
                        className="bg-blue-gray-900/10 text-blue-gray-900 shadow-none hover:scale-105 hover:shadow-none focus:scale-105 focus:shadow-none active:scale-100"
                    >
                        Add to Cart
                    </Button>
                </CardFooter>
            </Card>
        </>
    )
}

CourseCard.propTypes = {
    item: PropTypes.shape({
        id: PropTypes.number.isRequired,
        subject: PropTypes.string.isRequired,
        image: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
        category: PropTypes.string.isRequired
    }).isRequired
}

export default CourseCard