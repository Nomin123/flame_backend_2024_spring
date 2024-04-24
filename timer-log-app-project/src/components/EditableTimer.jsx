
import { useState } from "react";
import Timer from "./Timer";
import ToggleableTimerForm from "./ToggleableTimerForm";

function EditableTimer(props) {
    const [editFormOpen, setEditFormOpen] = useState(false)

    if(editFormOpen){
        return (
            <ToggleableTimerForm
                id={props.id}
                title={props.title}
                project={props.project}
            />
        );
    }else{
        return (
            <Timer
                id={props.id}
                title={props.title}
                project={props.project}
                elapsed={props.elapsed}
                runningSince={props.runningSince}
            />
        );
    }
}
export default EditableTimer;
