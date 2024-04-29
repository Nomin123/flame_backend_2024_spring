import { useState } from "react";
import Timer from "./Timer";
import TimerForm from "./TimerForm";

export default function EditableTimer({
    id,
    title,
    project,
    elapsed,
    runningSince,
    onFormSubmit
}) {
    const [editFormOpen, setEditFormOpen] = useState(false)

    const handleEditClick = () => {
        openForm();
    };

    const handleFormClose = () => {
        closeForm();
    };

    const handleSubmit = (timer) => {
        onFormSubmit(timer);
        setEditFormOpen(false);
    }
    const closeForm = () => {
        setEditFormOpen(false);
    };

    const openForm = () => {
        setEditFormOpen(true);
    };

    return (
        <>
            {editFormOpen ? (
                <TimerForm
                    id={id}
                    title={title}
                    project={project}
                    onFormSubmit={handleSubmit}
                    onFormClose={handleFormClose}
                />
            ) : (
                <Timer
                    id={id}
                    title={title}
                    project={project}
                    elapsed={elapsed}
                    runningSince={runningSince}
                    onEditClick={handleEditClick}
                />
            )}

        </>

    );

}
