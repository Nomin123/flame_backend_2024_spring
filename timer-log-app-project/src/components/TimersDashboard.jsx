import EditableTimerList from "./EditableTimerList";
import {timersData} from '../data/timers';
import ToggleableTimerForm from "./ToggleableTimerForm";
import { useState } from "react";

export default function TimersDashboard() {
    const [timers, setTimers] = useState(timersData);
    return (
        <div className="text-center">
            <div className="flex flex-col">
            <EditableTimerList timers={timers} />
            <ToggleableTimerForm />
            </div>
        </div>
    );
}