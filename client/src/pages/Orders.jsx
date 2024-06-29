import Each from "@/components/common/Each";
import Loading from "@/components/common/Loading";
import useFetch from "@/hooks/customs/useFetch";
import endpoints from "@/services/endpoints";
import { formatPrice } from "@/utils/format";

const Orders = () => {
    const { data, isLoading, error } = useFetch(endpoints['orders']);

    if (isLoading) {
        return <Loading />;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <section>
            <h1>Orders</h1>

            {data && data.length > 0 ? (
                <Each
                    of={data}
                    render={(item, index) => (
                        <li key={index}>
                            <p>ID: #{item.id}</p>
                            <p>Active: {item.active && 'COMPLETED'}</p>
                            <Each
                                of={item.details}
                                render={(detail) => (
                                    <>
                                        <p>Course ID: #{detail.course.id}</p>
                                        <p>Subject: {detail.course.subject}</p>
                                        <p>Quantity: {detail.quantity}</p>
                                        <p>
                                            Price: {formatPrice(detail.unit_price)}
                                        </p>
                                    </>
                                )}
                            />
                            <p>
                                Total Price: {formatPrice(item.total_price)}
                            </p>
                        </li>
                    )}
                />
            ) : (
                <p>No items exists</p>
            )}
        </section>
    )
}

export default Orders