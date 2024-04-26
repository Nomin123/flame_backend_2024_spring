import EditableTimerList from "./EditableTimerList";
import { timersData } from '../data/timers';
import ToggleableTimerForm from "./ToggleableTimerForm";
import { useState } from "react";

export default function TimersDashboard() {
    const [timers, setTimers] = useState(timersData);

    const handleCeateFormSubmit = (timer) => {
        createTimer(timer);
    };
    const createTimer = (timer) => {
        const t = newTimer = (timer);
        setTimers([...timers, t]);
    };
    return (
        <div className="text-center">
            <div className="flex flex-col">
                <EditableTimerList timers={timers} />
                <ToggleableTimerForm onFormSubmit={handleCeateFormSubmit} />
            </div>
        </div>
    );
}