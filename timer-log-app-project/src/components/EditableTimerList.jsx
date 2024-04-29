import EditableTimer from "./EditableTimer";

const EditableTimerList = ({ timers, onFormSubmit }) => {
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
                    onFormSubmit={onFormSubmit}
                />
            ))}

        </div>
    );
};
export default EditableTimerList;