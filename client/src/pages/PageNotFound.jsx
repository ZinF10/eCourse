import useDocumentTitle from "@/hooks/customs/useDocumentTitle"

const PageNotFound = () => {
    useDocumentTitle('Page Not Found - eCourse 🎓')

    return (
        <section>404 - Page Not Found</section>
    )
}

export default PageNotFound