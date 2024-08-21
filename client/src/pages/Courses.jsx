import Title from "@/components/ui/atoms/Title"
import CourseList from "@/components/ui/organisms/CourseList"

const Courses = () => {
    return (
        <section className="py-2">
            <Title>Courses</Title>
            <CourseList />
        </section>
    )
}

export default Courses