import Timer from "./Timer";
import TimerForm from "./TimerForm";

export default function EditableTimer(props) {
    if (props.editFormOpen) {
        return (
            <TimerForm
                title={props.title}
                project={props.project}
            />
        );
    } else {
        return (
            <Timer
                title={props.title}
                project={props.project}
                elapsed={props.elapsed}
                runningSince={props.runningSince}
            />
        );
    }
}