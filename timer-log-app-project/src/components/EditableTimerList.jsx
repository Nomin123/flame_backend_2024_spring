import EditableTimer from "./EditableTimer";

const EditableTimerList = ({ timers }) => {
    return (
        <div id='timers'>
            {timers.map((timer) => (
                <EditableTimer
                    key={timer.id}
                    id={timer.id}
                    title={timer.title}
                    project={timer.project}
                    elapsed={timer.elapsed}
                    runningSince={timer.runningSince}
                />
            ))}

        </div>
    );
};
export default EditableTimerList;