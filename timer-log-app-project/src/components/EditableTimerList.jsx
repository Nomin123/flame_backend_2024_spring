import EditableTimer from "./EditableTimer";


export default function EditableTimerList(props) {
    const timers = props.timers.map(timer =>
        <EditableTimer
            key={timer.id}
            id={timer.id}
            title={timer.title}
            project={timer.project}
            elapsed={timer.elapsed}
            runningSince={timer.runningSince}
        />
    )
    return (
        <div id='timers'>
            {timers}
        </div>
    );
}