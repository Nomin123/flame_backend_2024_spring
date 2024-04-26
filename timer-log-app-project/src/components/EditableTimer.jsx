import { useState } from "react";
import Timer from "./Timer";
import TimerForm from "./TimerForm";

export default function EditableTimer({
    id,
    title,
    project,
    elapsed,
    runningSince,
}) {
    const [editFormOpen, setEditFormOpen] = useState(false)

    return (
        <>
            {editFormOpen ? (
                <TimerForm id={id} title={title} project={project} />
            ) : (
                <Timer
                    id={id}
                    title={title}
                    project={project}
                    elapsed={elapsed}
                    runningSince={runningSince}
                />
            )}

        </>

    );

}
