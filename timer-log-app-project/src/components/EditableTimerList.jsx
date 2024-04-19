import EditableTimer from "./EditableTimer";

export default function EditableTimerList() {
    return (
        <div id='timers'>
            <EditableTimer
                title='Learn React'
                project='Web Domimation'
                elapsed='8986300'
                runningSince={null}
                editFormOpen={false}
            />
            <EditableTimer
                title='Learn extreme ironing'
                project='World Domimation'
                elapsed='3890985'
                runningSince={null}
                editFormOpen={true}
            />
        </div>
    );
}