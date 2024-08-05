import moment from 'moment';

const formatPrice = (price) => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
    }).format(price);
};

const formatFullName = (firstName, lastName) => {
    return `${lastName} ${firstName}`
};

const formatMoment = (date) => {
    return moment(date).fromNow()
}

export { formatPrice, formatFullName, formatMoment }